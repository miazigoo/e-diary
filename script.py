from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject)
import random

COMMENDATIONS = ['Молодец!', 'Отлично!', 'Хорошо!',
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


def get_schoolkid(schoolkid):
    try:
        child = Schoolkid.objects.filter(full_name__contains=schoolkid).get()
        return child
    except Schoolkid.MultipleObjectsReturned and Schoolkid.DoesNotExist:
        print('Такого ученика не существует в этой школе. Либо Учеников с похожим именем больше одного.')
        quit()


def fix_marks(schoolkid):
    """ Изменить плохие оценки ученика на 5 """
    child = get_schoolkid(schoolkid)
    Mark.objects.filter(schoolkid=child, points__in=[2, 3]).update(points=5)
    return 'Поздравляю! Оценки исправлены! (^◔ᴥ◔^) '


def fix_chastisements(schoolkid):
    """ Удалить замечания """
    child = get_schoolkid(schoolkid)
    Chastisement.objects.filter(schoolkid=child).delete()
    return 'Поздравляю! Замечания удалены (◑‿◐)'


def create_commendation(name='', subject=''):
    """ Записать похвалу """
    try:
        schoolkid = get_schoolkid(name)
        less = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter,
                                     subject__title__contains=subject).order_by('-date').first()
        random_commendation = random.choice(COMMENDATIONS)
        Commendation.objects.create(schoolkid=schoolkid, subject=less.subject,
                                    teacher=less.teacher, created=less.date,
                                    text=random_commendation)
        return 'О, молодой хакер, похвала за урок записана! (✪‿✪)ノ '
    except Lesson.DoesNotExist:
        return 'Ученика или предмета не существует  ｡ﾟ･ (>﹏<) ･ﾟ｡ '
