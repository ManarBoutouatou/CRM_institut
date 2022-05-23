from ast import Return
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView, 
    FormView
)
from project.models import Project
from contact.models import Company, Employee, Lead
from django.contrib import messages
# Create your views here.
#Dashboard


class IndexView(TemplateView):
    template_name= "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["projects"] = Project.objects.all().order_by('started_date')
        context["subscriptions"] = Project.objects.all().order_by('contract_expiration')
        context["project_count"] =Project.objects.all().count()
        context["companies"] = Company.objects.all().order_by('collab_start')
        context["company_count"] =Company.objects.all().count()
        context["employees"] = Employee.objects.all().order_by('collab_start')
        context["client_count"] =Employee.objects.all().count()
        context["leads"] = Lead.objects.all().order_by('status')
        context["lead_count"] =Lead.objects.all().count()
        return context 

def typeView(request):
    ec= Project.objects.filter(project_type='e-commerce').count()
    ec =int(ec)
    ws= Project.objects.filter(project_type='web site').count()
    ws =int(ws)
    wa= Project.objects.filter(project_type='web app').count()
    wa =int(wa)
    project_type_list=['e-commerce','web site' ,'web app' ]
    number_list=['ec','ws' ,'wa' ]
    context= {'project_type_list': project_type_list,'number_list': number_list }
    return render('core:index.html', context)




