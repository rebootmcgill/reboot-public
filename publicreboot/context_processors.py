from publicreboot.models import OfficeHours

def office_hours(request):
    return {'office_hours': OfficeHours.objects.all()}
