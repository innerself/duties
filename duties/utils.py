from calendar import Calendar
from typing import List, Dict


def generate_calendar(years: List[int]) -> Dict[int, List]:
    return {year: Calendar().yeardatescalendar(year, width=12)[0] for year in years}
