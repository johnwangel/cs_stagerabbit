from django.db import models
from django.forms import ModelForm

# Create your models here.
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=14)
    abbr = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Theater(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    state = models.ForeignKey(State, related_name='states', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Production(models.Model):
    theater = models.ForeignKey(Theater, related_name='theaters', on_delete=models.CASCADE)
    show = models.CharField(max_length=600)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    venue = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.show

class NewProductionForm(ModelForm):
    class Meta:
        model = Production
        fields = ['theater', 'show', 'start_date', 'end_date', 'venue', 'description']