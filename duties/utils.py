import random
from calendar import Calendar
from typing import List, Dict

import mimesis
from django.contrib.auth.models import User
from mimesis import Text
from mimesis.enums import Gender


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


def random_color():
    text = Text()
    return text.hex_color()
