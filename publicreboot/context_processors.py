from publicreboot.models import OfficeHours, get_next_holiday, get_current_holiday


def office_hours(request):
    return {'office_hours': OfficeHours.objects.all()}


def holidays(request):
    return {'holiday': get_current_holiday(), 'next_holiday': get_next_holiday()}