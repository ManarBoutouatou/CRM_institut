from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, request
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
from django.views.generic.edit import CreateView
from pprint import pprint
from contact.models import Company, Employee
import project
from project.models import Project
from project.forms import Project, AddProjectForm
from project.filters import ProjectFilter
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages
import logging
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('core:index')
    def handle_no_permission(self):
        return redirect(self.get_login_url())


#project    
class ProjectListView(RedirectPermissionRequiredMixin,ListView): 
    template_name= "project_list.html"
    model = Project 
    permission_required= 'project.view_project'
    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        # context["projects"] =Project.objects.all().order_by('active')
        context["project_count"] =Project.objects.all().count()
        filters=ProjectFilter(self.request.GET, queryset=Project.objects.all())
        context["projects"] = filters.qs
        return context
    
class ProjectDetailView(RedirectPermissionRequiredMixin,DetailView):
    model = Project
    template_name= "project_detail.html"
    permission_required= 'project.view_project'
  
        
class AddProjectView(RedirectPermissionRequiredMixin,SuccessMessageMixin, CreateView):
    template_name= "project_add.html"
    form_class= AddProjectForm
    model = Project
    success_message = "Project added successfully."
    permission_required= 'project.add_project'
    success_url = reverse_lazy('project:projectlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddProjectView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["employees"] = Employee.objects.all()
        return context
   
 
class ProjectUpdateView(RedirectPermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Project
    form_class= AddProjectForm
    template_name = 'project_edit.html' 
    success_message = "Project updated successfully."
    permission_required= 'project.change_project'
    success_url = reverse_lazy('project:projectlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["employees"] = Employee.objects.all()
        return context
   

class ProjectDeleteView(RedirectPermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Project
    template_name= "project_delete.html"
    success_message = "Product deleted successfully."
    permission_required= 'project.delete_project'
    success_url = reverse_lazy('project:projectlist')