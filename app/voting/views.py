from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Список_вопросов, Список_ПВИ, Дата_окончания_голосования
import datetime
from django.http import HttpResponse

# Create your views here.

def vote_list(request):
    
    return render(request, "index.html")

def index(request):
    if request.method == "POST":
        link = 'http://127.0.0.1:8000/'
        vote_date = request.COOKIES['vote_date']

        try:
            isVote = request.COOKIES['isVote']

            if isVote:
                data = {
                "link" : link,
                "text" : "Вы уже голосовали",
                }
                return render(request, "answer.html", context=data)
        except:
            pass

        date = Дата_окончания_голосования.objects.all()
        end_date = str(date[0])
        num_1_day, num_1_mounth, = vote_date[3:], vote_date[:2]
        num_2_day, num_2_mounth, = end_date[8:10], end_date[5:7]

        if num_1_mounth <= num_2_mounth:
            if num_1_day <= num_2_day:
                status = "OK"
            else:
                status = "NOT_OK"
        else:
                status = "NOT_OK"

        if status == "NOT_OK":
            data = {
            "link" : link,
            "text" : "Данный опрос завершился " + end_date,
            }
            return render(request, "answer.html", context=data)
        else:
            d1 = datetime.datetime.strptime(str(num_1_day)+"."+ str(num_1_mounth) +".2020", "%d.%m.%Y") # vote day
            d2 = datetime.datetime.strptime(str(num_2_day)+"."+ str(num_2_mounth) +".2020", "%d.%m.%Y") # end day для расчета длительнсти куки
            days_expire = (d2 - d1).days
            data = {
                "link" : link,
                "days_expire" : "До конца опроса осталось " +str(days_expire)+ " суток",
                "date" : num_2_mounth,
            }#2020-11-18
            response = HttpResponse(render(request, "answer.html", context=data))
            if days_expire > 0:
                response.set_cookie("isVote", True, max_age=60*60*24*days_expire)
            else:
                response.set_cookie("isVote", True, max_age=60*60*10)


            return response
    else:
        now = datetime.datetime.now()

        questions_list = Список_вопросов.objects.all()
        PVI_list = Список_ПВИ.objects.all()

        data = {
            "PVI" : PVI_list,
            "questions_list" : questions_list,
            "current_date" : now.strftime("%d-%m-%Y"),

        }

        return render(request, "index.html", context=data)