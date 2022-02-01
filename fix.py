import random

from datacenter.models import Lesson, Schoolkid, Mark, Chastisement, Subject

ivan = Schoolkid.objects.get(full_name__contains="Фролов Иван")


def fix_marks(schoolkid: Schoolkid) -> None:
    less_than_4_marks = Mark.objects.get(schoolkid=schoolkid, points__lt=4)
    for mark in less_than_4_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid: Schoolkid) -> None:
    chastisements = Chastisement.objects.get(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid: Schoolkid, subject_title: str) -> None:
    subject = Subject.objects.get(
        title=subject_title, year_of_study=schoolkid.year_of_study
    )
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject,
    )
    random_lesson = random.choice(lessons)
    chastisement_texts = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
    ]
    chastisement = Chastisement.objects.create(
        schoolkid=schoolkid,
        created=random_lesson.date,
        text=random.choice(chastisement_texts),
        subject=random_lesson.subject,
        teacher=random_lesson.teacher,
    )
