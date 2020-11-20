from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Список_вопросов, Список_ПВИ, Дата_окончания_голосования, Список_ответов, Общие_комментарии
import datetime
import random
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError  
import pandas as pd
from .forms import PasswordForm


def stats_login(request):
    form = PasswordForm(request.POST)
    if form.is_valid():
        if request.POST['password'] == "Qwerty2":  # PASSWORD KEK TO DO
            questions_query = Список_вопросов.objects.all()
            questions_list = []
            for question in questions_query:
                questions_list.append(question.question_text)
            answers_list= Список_ответов.objects.all()
            average_value = []
            
            

            for el in questions_list:
                average_value.append(random.randint(1, 5))

            value_and_question = []
            for i in range(len(average_value)):
                value_and_question.append([questions_list[i], average_value[i], i+1])
            
            data = {
                "questions" : questions_list,
                "answers" : answers_list,
                "value_and_question" : value_and_question,
            }

            return render(request, "stats.html", context=data)
        else:
            data = {
                "result" : False,
                'form': form,
            }
            return render(request, "stats_login.html", context=data)
    else:
        form = PasswordForm()
        data = {
                "result" : True,
                'form': form,
            }
        return render(request, 'stats_login.html', context=data)


def index(request):
    if request.method == "POST":
        #link = 'http://188.225.83.42:8000/'
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

            questions_query = Список_вопросов.objects.all()
            questions_list = []
            for question in questions_query:
                questions_list.append(question.question_text)
            try:
                answers_list = []
                comment_list = []
                for el in questions_list:
                    answers_list.append(request.POST[el+'_mark'])
                    comment_temp = str(request.POST[el+'_comment'])
                    if comment_temp == '': comment_list.append('None')
                    else : comment_list.append(comment_temp)
            except MultiValueDictKeyError:
                pass
            
            results = []
            unique_id = random.randint(0, 200000)
            try:
                for i in range(len(answers_list)):
                    results.append([questions_list[i], answers_list[i], comment_list[i]])
                    Список_ответов(Вопрос=questions_list[i], Оценка=answers_list[i], unique_key=unique_id, Комментарий=comment_list[i]).save()
            except:
                pass
            
            if str(request.POST['wishes_text']) != '': Общие_комментарии(unique_key=unique_id, Пожелание=str(request.POST['wishes_text'])).save()

            data = {
                "link" : link,
                "days_expire" : "До конца опроса осталось " +str(days_expire)+ " суток",
                "date" : num_2_mounth,
                "a" : results,
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