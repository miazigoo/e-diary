from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from models import Lesson
from models import Schoolkid
from models import Commendation
from models import Chastisement
from models import Mark
import random


def get_schoolkid(schoolkid):
    try:
        child = Schoolkid.objects.filter(full_name__contains=schoolkid).get()
        return child
    except MultipleObjectsReturned:
        return "Учеников с похожим именем больше одного  ༼☯﹏☯༽ . Сделайте запрос более подробным."



def fix_marks(schoolkid):
    """ Изменить плохие оценки ученика на 5 """
    try:
        child = get_schoolkid(schoolkid)
        bad_marks = Mark.objects.filter(schoolkid=child, points_in=[2, 3])
        for mark in bad_marks:
            mark.points = 5
            mark.save()
        return 'Поздравляю! Оценки исправлены! (^◔ᴥ◔^) '
    except MultipleObjectsReturned:
        return "Учеников с похожим именем больше одного  ༼☯﹏☯༽ . Сделайте запрос более подробным."


def fix_chastisements(schoolkid):
    """ Удалить замечания """
    try:
        child = get_schoolkid(schoolkid)
        chastisements = Chastisement.objects.filter(schoolkid=child)
        for chast in chastisements:
            chast.delete()
        return 'Поздравляю! Замечания удалены (◑‿◐)'
    except MultipleObjectsReturned:
        return "Учеников с похожим именем больше одного  (⋟﹏⋞) . Сделайте запрос более подробным."


def create_commendation(name='', subject=''):
    """ Записать похвалу """
    try:
        schoolkid = get_schoolkid(name)
        print(schoolkid)
        less = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter,
                                     subject__title__contains=subject).order_by('-date').first()
        commendation = ['Молодец!', 'Отлично!', 'Хорошо!',
                        'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                        'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!',
                        'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!',
                        'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!',
                        'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!',
                        'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!',
                        'Ты на верном пути!', 'Здорово!', 'Это как раз то, что нужно!',
                        'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
                        'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!',
                        'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
                        'Теперь у тебя точно все получится!', ]
        random_commendation = random.choice(commendation)
        print(random_commendation)
        Commendation.objects.create(schoolkid=schoolkid, subject=less.subject,
                                    teacher=less.teacher, created=less.date,
                                    text=random_commendation)
        return 'О, молодой хакер, похвала за урок записана! (✪‿✪)ノ '
    except ObjectDoesNotExist:
        return 'Ученика или предмета не существует  ｡ﾟ･ (>﹏<) ･ﾟ｡ '



