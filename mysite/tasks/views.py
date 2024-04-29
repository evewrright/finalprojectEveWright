from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .forms import TasksForm
from .models import Task
from django.urls import reverse, reverse_lazy


class TasksIndexView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        # Only retrieve tasks that were created by current user and aren't complete
        if self.request.user.is_authenticated:
            return Task.objects.filter(author_id=self.request.user, complete=False)
        else:
            return Task.objects.none()

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TasksDetailView(generic.DetailView):
    model = Task
    template_name = "tasks/detail.html"
    context_object_name = "task"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return redirect('tasks:index')
        return super().dispatch(request, *args, **kwargs)


class TasksCreateView(generic.CreateView):
    model = Task
    form_class = TasksForm
    template_name = "tasks/create.html"

    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksUpdateView(generic.UpdateView):
    model = Task
    form_class = TasksForm
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks:index")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return redirect('tasks:index')
        return super().dispatch(request, *args, **kwargs)


class TasksDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/index.html"
    success_url = reverse_lazy("tasks:index")


def mark_complete(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.complete = True
        task.save()
        return HttpResponseRedirect(reverse('tasks:index'))
