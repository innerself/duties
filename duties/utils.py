import datetime
import random
from calendar import Calendar
from typing import List, Dict

import mimesis
from django.contrib.auth.models import User
from mimesis.enums import Gender

from duties import models


def generate_calendar(years: List[int]) -> Dict[int, List]:
    return {year: Calendar().yeardatescalendar(year, width=12)[0] for year in years}


def generate_user():
    person = mimesis.Person(locale='ru')
    gender = random.choice([Gender.MALE, Gender.FEMALE])

    return User(
        username=person.username(),
        password=person.password(),
        first_name=person.first_name(gender=gender),
        last_name=person.last_name(gender=gender),
        email=person.email(),
    )


def generate_users(number: int = 5) -> List[User]:
    return [generate_user() for _ in range(number)]


def random_color() -> str:
    return mimesis.Text().hex_color()


def generate_duty_date(unique: bool = True):
    mim_datetime = mimesis.Datetime()

    year_objects = models.CalendarYear.objects.all()

    if year_objects:
        years = [x.year for x in year_objects]
    else:
        years = [datetime.date.today().year]

    while True:
        dt = mim_datetime.date(start=min(years), end=max(years))
        if not unique or not models.DutyDate.objects.filter(date=dt).exists():
            break

    return models.DutyDate(date=dt)


def generate_duties(user, number: int = 50):
    for _ in range(number):
        duty_date = generate_duty_date()
        duty_date.save()
        user.profile.duties.add(duty_date)

    user.save()
