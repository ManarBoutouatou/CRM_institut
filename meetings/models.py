from datetime import datetime
from django.db import models
from django.urls import reverse
from contact.models import Company, Employee
# Create your models here.

class Event(models.Model):
    title        = models.CharField(max_length=200)
    description  = models.TextField()
    start_date   = models.DateField()
    start_time   = models.TimeField(blank=True, null=True,)
    end_time     = models.TimeField(blank=True, null=True,)
    company      = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE) 
    manager      = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    @property
    def get_html_url(self):
        url = reverse('meetings:event_edit', args=(self.id,))
        return f'<a href="{url}" style="text-decoration:none; color:#392C70;"> {self.title} </a>'

    

    