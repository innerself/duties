from django.contrib import admin

from duties.models import Profile, CalendarYear, DutyDate

admin.site.register(Profile)
admin.site.register(CalendarYear)
admin.site.register(DutyDate)
