from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import EventCreateForm, EventUpdateForm
from events.models import Event


class EventListView(ListView):
    template_name = 'events/list.html'
    model = Event
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.get_all_events()

    def get_context_data(self):
        context = super(EventListView, self).get_context_data()
        return context


class EventCreateView(CreateView):
    template_name = 'events/create.html'
    model = Event
    form_class = EventCreateForm

    def get_context_data(self, **kwargs):
        context = super(EventCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        event = form.save()
        messages.success(self.request, 'Event {} has been successfully added.'.format(event.title))
        return super(EventCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('events:list')
        if self.request.POST.get('_addanother'):
            return reverse_lazy('events:create')


class EventUpdateView(UpdateView):
    template_name = 'events/update.html'
    model = Event
    form_class = EventUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(EventUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        event = form.save()
        messages.success(self.request, 'Event \"{}\" has been successfully updated.'.format(event.title))
        return super(EventUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('events:list')


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('events:list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(EventDeleteView, self).post(request, *args, **kwargs)
