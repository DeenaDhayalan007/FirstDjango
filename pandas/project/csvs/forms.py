from django import forms
from django.db import models
from django.db.models import fields
from .models import Csv

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ['file_name',]
