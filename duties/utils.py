from calendar import Calendar
from collections import namedtuple


Day = namedtuple(
    'CalendarDay',
    ['date', 'is_in_current_month', 'day_num', 'weekday'],
)


class DutyCalendar:
    def draw_calendar(self, year) -> str:
        html_calendar = list()
        raw_calendar = self._generate_calendar(year)

        # TODO Prettify HTML properly
        indent = 0
        html_calendar.append(f'{" " * indent}<div id="{year}" class="year">')
        html_calendar.extend([self._format_month(month, indent + 4) for month in raw_calendar])
        html_calendar.append('</div>')

        return ''.join(html_calendar)

    def _format_month(self, month, base_indent):
        indent = base_indent + 2
        html_month = list()

        html_month.append(f'\n{" " * indent}<div class="month">')
        html_month.extend([self._format_week(week, indent) for week in month])
        html_month.append(f'\n{" " * indent}</div>')

        return ''.join(html_month)

    def _format_week(self, week, base_indent):
        indent = base_indent + 2
        html_week = list()

        html_week.append(f'\n{" " * indent}<div class="week">')
        html_week.extend([self._format_day(day, indent) for day in week])
        html_week.append(f'\n{" " * indent}</div>')

        return ''.join(html_week)

    def _format_day(self, day, base_indent):
        indent = base_indent + 2

        if day.is_in_current_month:
            html_day = f'\n{" " * indent}<div id="{day.date.isoformat()}" class="day">{day.day_num}</div>'
        else:
            html_day = f'\n{" " * indent}<div class="day">&nbsp</div>'

        return html_day

    def _generate_calendar(self, year: int):
        dates_calendar = Calendar().yeardatescalendar(year, width=12)
        days_calendar = Calendar().yeardays2calendar(year, width=12)
        calendar_data_sequence = enumerate(zip(dates_calendar[0], days_calendar[0]), 1)

        return [
            self._generate_month(month_num, month_dates, month_days)
            for month_num, (month_dates, month_days)
            in calendar_data_sequence
        ]

    def _generate_month(self, month_num, month_dates, month_days):
        return [
            self._generate_week(week_dates, week_days)
            for week_dates, week_days in
            zip(month_dates, month_days)
        ]

    def _generate_week(self, week_dates, week_days):
        return [
            self._generate_day(dates_day, days_day)
            for dates_day, days_day
            in zip(week_dates, week_days)
        ]

    def _generate_day(self, dates_day, days_day):
        return Day(
            date=dates_day,
            is_in_current_month=bool(days_day[0]),
            day_num=days_day[0],
            weekday=days_day[1],
        )
