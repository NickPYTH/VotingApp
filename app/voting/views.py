from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse
from .models import Список_вопросов, Список_ПВИ, Дата_окончания_голосования, Список_ответов, Общие_комментарии
import datetime
import random
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError  
import pandas as pd
from .forms import PasswordForm
from django.core.files.storage import FileSystemStorage



def get_stats(request):
    answers_list= Список_ответов.objects.all()
    questions_list= Список_вопросов.objects.all()
    pvi_list = Список_ПВИ.objects.all()
    comments_list = Общие_комментарии.objects.all()

    questions_dict = {
        "Номер_Вопроса" : [el+1 for el in range(len(questions_list))],
        "Вопрос":[el.question_text for el in questions_list],
        "Дата создания":[el.date for el in questions_list],
            }
    questions_table = pd.DataFrame(questions_dict)
    
    answers_dict = {
        "unique_key":[el.unique_key for el in answers_list],
        "Вопрос":[el.Вопрос for el in answers_list],
        "Оценка":[el.Оценка for el in answers_list],
        "Комментарий":[el.Комментарий for el in answers_list],
        "Дата":[el.Дата for el in answers_list],
        "ПВИ":[el.ПВИ for el in answers_list],
        
            }
    answers_table = pd.DataFrame(answers_dict) 
    pvi_dict = {
        "Название_ПВИ":[el.Название_ПВИ for el in pvi_list],
        "Местонахождение_ПВИ":[el.Местонахождение_ПВИ for el in pvi_list],
            }
    pvi_table = pd.DataFrame(pvi_dict)

    comments_dict = {
        "unique_key":[el.unique_key for el in comments_list],
        "Пожелание":[el.Пожелание for el in comments_list],
            }
    comments_table = pd.DataFrame(comments_dict)

    writer = pd.ExcelWriter('out.xlsx', engine = 'xlsxwriter')
    questions_table.to_excel(writer, sheet_name = 'Вопросы')
    answers_table.to_excel(writer, sheet_name = 'Ответы')
    pvi_table.to_excel(writer, sheet_name = 'ПВИ')
    comments_table.to_excel(writer, sheet_name = 'Комментарии')
    writer.save()

    writer = pd.ExcelWriter('mediafiles/out.xlsx', engine = 'xlsxwriter')
    questions_table.to_excel(writer, sheet_name = 'Вопросы')
    answers_table.to_excel(writer, sheet_name = 'Ответы')
    pvi_table.to_excel(writer, sheet_name = 'ПВИ')
    comments_table.to_excel(writer, sheet_name = 'Комментарии')
    writer.save()
    
    file_path = os.path.join(settings.MEDIA_ROOT, 'out.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return render(request, "download.html")

    return render(request, "download.html")



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
        
            for ques in questions_list:
                temp = Список_ответов.objects.filter(Вопрос=ques)
                if len(temp) != 0:
                    av_val_tmp = 0
                    counter = 0
                    for el in temp:
                        av_val_tmp += el.Оценка
                        counter += 1
                    average_value.append([ques, round(float(av_val_tmp/counter), 1)])

            pvi_query = Список_ПВИ.objects.all()
            pvi_list = [pvi.Название_ПВИ for pvi in pvi_query]
            
            out = []
            ques_and_average = []
            for pvi in pvi_list:
                ans_tmp = Список_ответов.objects.filter(ПВИ=pvi)
                average_temp = 0
                if len(ans_tmp) > 0:
                    for i in range(len(questions_list)):
                        ans_tmp_ques = ans_tmp.filter(Вопрос=questions_list[i])
                        for el in ans_tmp_ques:
                            average_temp += el.Оценка
                        if len(ans_tmp_ques) != 0:
                            average_temp /= len(ans_tmp_ques)
                        ques_and_average.append([questions_list[i], round(float(average_temp), 1)])
                        average_temp = 0
                    out.append([pvi, ques_and_average, random.randint(0, 10000)])
                    ques_and_average = []
            data = {
                "questions" : questions_list,
                "answers" : answers_list,
                "value_and_question" : average_value,
                "out" : out,
                'link' : settings.INDEX_LINK,  
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
                'form' : form,
                'link' : settings.INDEX_LINK,  
            }
        return render(request, 'stats_login.html', context=data)

def vote_date_check(request, date):  # если фалс, то сменить дату окончания в куках
    try:
        old_date = request.COOKIES['end_date']
        end_date = str(date[0])
        num_end_day, num_end_mounth = end_date[8:10], end_date[5:7]
        num_current_day, num_current_mounth, = old_date[0:2], old_date[3:5]
        print(num_current_day, num_current_mounth, num_end_day, num_end_mounth)                                                
        if num_current_mounth < num_end_mounth:
            return [True, str(num_end_day) + '.' + str(num_end_mounth)]
        elif num_current_mounth == num_end_mounth:
            if num_current_day < num_end_day:
                return [False, str(num_end_day) + '.' + str(num_end_mounth)]
            else:
                return [True, str(num_end_day) + '.' + str(num_end_mounth)]
        else:
            return [False, str(num_end_day) + '.' + str(num_end_mounth)]

            
    except:
        return [True, None]

def index(request):
    if request.method == "POST":
        vote_date = request.COOKIES['vote_date']

        date = Дата_окончания_голосования.objects.all()
        tmp = vote_date_check(request, date)
        upd_date = False
        if not tmp[0]:
            #print('-----------------> Дата окончания голосования изменилась')
            upd_date = True
        else:
            #print('-----------------> Дата окончания голосования НЕ изменилась')
            pass

        try:
            isVote = request.COOKIES['isVote']
            if isVote and tmp[0]:
                data = {
                "link" : settings.INDEX_LINK,
                "text" : "Вы уже голосовали",
                }
                response = HttpResponse(render(request, "answer.html", context=data))
                if upd_date:
                    response.set_cookie("end_date", tmp[1], max_age=60*60*24*60)  # утстановка в куки даты голосвания для проверки е изменения
                else:
                    response.set_cookie("end_date", tmp[1], max_age=60*60*24*60)  # утстановка в куки даты голосвания для проверки е изменения
                return response
        except:
            pass


        end_date = str(date[0])
        num_1_day, num_1_mounth, = int(vote_date[3:]), int(vote_date[:2])
        num_2_day, num_2_mounth, = int(end_date[8:10]), int(end_date[5:7])
        
        if num_1_mounth <= num_2_mounth:
            if num_1_day <= num_2_day and num_1_mounth == num_2_mounth:
                status = "OK"
            elif num_1_mounth < num_2_mounth:
                status = "OK"
            else:
                status = "NOT_OK"
        else:
                status = "NOT_OK"


        if status == "NOT_OK":
            data = {
            "link" : settings.INDEX_LINK,
            "text" : "Данный опрос завершился " + end_date,
            }

            response = HttpResponse(render(request, "answer.html", context=data))
            if upd_date:
                d1 = datetime.datetime.strptime(str(num_1_day)+"."+ str(num_1_mounth) +".2020", "%d.%m.%Y") # vote day
                d2 = datetime.datetime.strptime(str(num_2_day)+"."+ str(num_2_mounth) +".2020", "%d.%m.%Y") # end of vote day
                days_expire = (d2-d1).days
                response.set_cookie("end_date", tmp[1], max_age=60*60*24*days_expire)  # утстановка в куки даты голосвания для проверки е изменения
            else:
                response.set_cookie("end_date", str(num_2_day)+"."+ str(num_2_mounth), max_age=60*60*24)  # утстановка в куки даты голосвания для проверки е изменения
            return response

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
            unique_id = random.randint(0, 300000)
            try:
                for i in range(len(answers_list)):
                    results.append([questions_list[i], answers_list[i], comment_list[i]])
                    Список_ответов(Вопрос=questions_list[i], Оценка=answers_list[i], unique_key=unique_id, Комментарий=comment_list[i], ПВИ=str(request.POST['select_pvi'])).save()
            except:
                pass
            
            if str(request.POST['wishes_text']) != '': Общие_комментарии(unique_key=unique_id, Пожелание=str(request.POST['wishes_text'])).save()

            data = {
                "link" : settings.INDEX_LINK,
                "days_expire" : "До конца опроса осталось " +str(days_expire)+ " суток",
                "date" : num_2_mounth,
                "a" : results,
            }#2020-11-18

            


            response = HttpResponse(render(request, "answer.html", context=data))
            if days_expire > 0:
                response.set_cookie("isVote", True, max_age=60*60*24*days_expire)
                if upd_date:
                    response.set_cookie("end_date", tmp[1], max_age=60*60*24*days_expire)  # утстановка в куки даты голосвания для проверки е изменения
                else:
                    response.set_cookie("end_date", str(num_2_day)+"."+ str(num_2_mounth), max_age=60*60*24*days_expire)  # утстановка в куки даты голосвания для проверки е изменения
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
