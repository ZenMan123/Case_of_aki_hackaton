import datetime
from django.utils import timezone
from organizers.models import Entry
from platforms.models import FreeSlot

WEEKDAYS = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
MONTHS = ['Январь',
          'Февраль',
          'Март',
          'Апрель',
          'Май',
          'Июнь',
          'Июль',
          'Август',
          'Сентябрь',
          'Октябрь',
          'Ноябрь',
          'Декабрь']
HUMANIZED_MONTHS = ['Января',
                    'Февраля',
                    'Марта',
                    'Апреля',
                    'Мая',
                    'Июня',
                    'Июля',
                    'Августа',
                    'Сентября',
                    'Октября',
                    'Ноября',
                    'Декабря']


class Slot:
    def __init__(self, date, price, time_comparison, is_booked):
        self.day = date.day
        self.month = HUMANIZED_MONTHS[date.month - 1]
        self.price = price
        self.weekday = date.weekday()
        self.time_comparison = time_comparison
        self.is_booked = is_booked


class Month:
    def __init__(self, tmp, today, free_slots, entries):
        self.tmp = tmp
        self.month = MONTHS[tmp.month - 1]
        self.weeks = []
        for week_delta in range(-5, 6):
            self.add_week(self.tmp + datetime.timedelta(weeks=week_delta), today, free_slots, entries)

    @staticmethod
    def get_next_sunday(date):
        weekday = date.weekday()
        return date + datetime.timedelta(days=6 - weekday)

    @staticmethod
    def get_prev_monday(date):
        weekday = date.weekday()
        return date + datetime.timedelta(days=-weekday)

    def add_week(self, date, today, free_slots, entries):
        if self.get_next_sunday(date).month < self.tmp.month or self.get_prev_monday(date).month > self.tmp.month:
            return

        week_slots = []

        for weekday in range(7):
            delta = weekday - date.weekday()
            tmp_date = date + datetime.timedelta(delta)

            if tmp_date < today:
                time_comparison = 'less'
            elif tmp_date == today:
                time_comparison = 'equal'
            else:
                time_comparison = 'more'

            if entries.filter(date=tmp_date).exists():
                is_booked = True
            else:
                is_booked = False

            week_slots.append(Slot(tmp_date, 1000, time_comparison, is_booked))

        self.weeks.append(week_slots)


def build_calendar(platform_id):
    today = datetime.date(year=timezone.now().year, month=timezone.now().month, day=timezone.now().day)

    free_slots = FreeSlot.objects.filter(platform_id=platform_id)
    entries = Entry.objects.filter(platform_id=platform_id)

    months = []
    tmp = today
    for i in range(3):
        months.append(Month(tmp, today, free_slots, entries))
        if tmp.month == 12:
            tmp = datetime.date(tmp.year + 1, 1, 1)
        else:
            tmp = datetime.date(tmp.year, tmp.month + 1, 1)

    return months