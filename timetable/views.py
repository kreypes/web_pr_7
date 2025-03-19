
from django.http import HttpResponse

ttemplate = '<div style="font-size: 30px;">Расписание занятий на'
ttable = [
    ['Информатика', 'Физкультура', 'Литература', 'Русский язык'],
    ['Информатика', 'Математика', 'Литература', 'География'],
    ['Физкультура', 'Математика', 'Математика', 'Русский язык'],
    ['Математика', 'Информатика', 'Литература', 'Биология'],
    ['Литература', 'Математика', 'Информатика', 'Физкультура']
]

def lessons(week, ttable):
    if ttable is not None:
        count = 1
        lessons = ''
        for lesson in ttable:
            lessons += f'<b>{count}.</b> {lesson}<br>'
            count += 1
        return HttpResponse(f'<b>{ttemplate} {week}:</b><br><br>{lessons}</div>')
    else:
        return HttpResponse(f'<b>{ttemplate} {week}:</b><br><br>Выходной.</div>')
def monday(request):
    return HttpResponse(lessons('Понедельник', ttable[0]))
def tuesday(request):
    return HttpResponse(lessons('Вторник', ttable[1]))

def wednesday(request):
    return HttpResponse(lessons('Среду', ttable[2]))

def thursday(request):
    return HttpResponse(lessons('Четверг', ttable[3]))

def friday(request):
    return HttpResponse(lessons('Пятницу', ttable[4]))

def saturday(request):
    return HttpResponse(lessons('Субботу', None))

def sunday(request):
    return HttpResponse(lessons('Воскресенье', None))