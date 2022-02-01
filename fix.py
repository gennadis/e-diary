from random import choice
from typing import Optional

from datacenter.models import Lesson, Schoolkid, Mark, Chastisement, Subject


def get_schoolkid(full_name: str) -> Optional[Schoolkid]:
    try:
        return Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        print("Schoolkid doesn't exist.")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"There are several schoolkids with name like {full_name}.")
        return


def fix_marks(schoolkid: Schoolkid) -> None:
    less_than_4_marks = Mark.objects.get(schoolkid=schoolkid, points__lt=4)
    for mark in less_than_4_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid: Schoolkid) -> None:
    Chastisement.objects.get(schoolkid=schoolkid).delete()


def create_commendation(schoolkid: Schoolkid, subject_title: str) -> None:
    try:
        subject = Subject.objects.get(
            title=subject_title, year_of_study=schoolkid.year_of_study
        )
    except (Subject.DoesNotExist, Subject.MultipleObjectsReturned):
        print(f"Please scecify subject title.")
        return

    subject_lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject,
    )
    random_lesson = choice(subject_lessons)

    chastisement_phrases = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
    ]

    Chastisement.objects.create(
        schoolkid=schoolkid,
        created=random_lesson.date,
        text=choice(chastisement_phrases),
        subject=random_lesson.subject,
        teacher=random_lesson.teacher,
    )
