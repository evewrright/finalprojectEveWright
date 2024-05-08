from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Appointment
from django.urls import reverse, reverse_lazy
from .forms import ApptsForm
import requests
from django.http import JsonResponse
from datetime import datetime


class ApptsIndexView(generic.ListView):
    model = Appointment
    template_name = "appts/index.html"
    context_object_name = "appointments"

    def get_queryset(self):
        queryset = {'prev_appointments': Appointment.objects.exclude(occurred__gte=datetime.now()),
                    'future_appointments': Appointment.objects.filter(occurred__gte=datetime.now())}
        return queryset

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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


def generate_paragraph(request):
    if request.method == 'POST':
        input_text = request.POST.get('inputTextArea')
        url = "https://chatgpt-api8.p.rapidapi.com/"
        headers = {
            'content-type': 'application/json',
            'X-RapidAPI-Key': 'your_api_key',
            'X-RapidAPI-Host': 'chatgpt-api8.p.rapidapi.com'
        }
        payload = [
            {
                "content": 'turn these notes about a student into a paragraph with all complete sentences' + input_text,
                "role": "user"
            }
        ]
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            paragraph = response.json().get('text', None)
            return render(request, 'appts/paragraph.html', {'paragraph': paragraph})

    return HttpResponse()


class ParagraphView (generic.TemplateView):
    template_name = 'appts/paragraph.html'


def historyview(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if start_date and end_date:
            filtered_appointments = Appointment.objects.filter(occurred__range=(start_date, end_date))
            return render(request, 'appts/history.html', {'myappointments': filtered_appointments})
        else:
            appointments = Appointment.objects.all()
            return render(request, 'appts/history.html', {'myappointments': appointments})
    else:
        appointments = Appointment.objects.all()
        return render(request, 'appts/history.html', {'myappointments': appointments})
