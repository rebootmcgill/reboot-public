from django.shortcuts import render
from machinerequests.models import Request
from django.views.generic import CreateView

# Create your views here.

class RequestCreate(CreateView):
    model = Request
    fields = ['given_name', 'family_name', 'email', 'requester_type', 'faculty_and_dept', 'organization', 'preset', 'os', 'machine_use', 'need_display', 'need_mouse', 'need_keyboard', 'need_ethernet', 'extra_information', 'amount']
