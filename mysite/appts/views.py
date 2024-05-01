from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Appointment
from django.urls import reverse, reverse_lazy


class ApptsIndexView(generic.ListView):
    model = Appointment
    template_name = "appts/index.html"
    context_object_name = "appointments"
