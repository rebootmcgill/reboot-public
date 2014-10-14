from django.shortcuts import render
from machinerequests.models import Request
from publicreboot.models import OfficeHours
from django.views.generic import CreateView, base.TemplateView as TemplateView, DetailView

# Create your views here.

class RequestCreate(CreateView):
    model = Request
    template_name = "publicreboot/request.html"
    fields = ['given_name', 'family_name', 'email', 'requester_type', 'faculty_and_dept', 'organization', 'preset', 'os', 'machine_use', 'need_display', 'need_mouse', 'need_keyboard', 'need_ethernet', 'extra_information', 'amount']

class RecyclingView(TemplateView):
    template_name = "publicreboot/recycling.html"

class AboutView(DetailView):
    template_name = "publicreboot/about.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['office_hours'] = OfficeHours.objects.all()
        return context
