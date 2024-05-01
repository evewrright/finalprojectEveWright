from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Appointment
from django.urls import reverse, reverse_lazy
from .forms import ApptsForm


class ApptsIndexView(generic.ListView):
    model = Appointment
    template_name = "appts/index.html"
    context_object_name = "appointments"


class ApptsDetailView(generic.DetailView):
    model = Appointment
    template_name = "appts/detail.html"
    context_object_name = "appointment"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return redirect('appts:index')
        return super().dispatch(request, *args, **kwargs)


class ApptsCreateView(generic.CreateView):
    model = Appointment
    form_class = ApptsForm
    template_name = "appts/create.html"

    success_url = reverse_lazy("appts:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ApptsUpdateView(generic.UpdateView):
    model = Appointment
    form_class = ApptsForm
    template_name = "appts/update.html"
    success_url = reverse_lazy("appts:index")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return redirect('appts:index')
        return super().dispatch(request, *args, **kwargs)


class ApptsDeleteView(generic.DeleteView):
    model = Appointment
    template_name = "appts/index.html"
    success_url = reverse_lazy("appts:index")
