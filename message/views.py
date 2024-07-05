from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Message
from django.urls import reverse_lazy

# Create your views here.
class MessageList(ListView):
    model = Message


class MessageRead(DetailView):
    model = Message
    field = ['user', 'receipt', 'subject', 'content']
    success_urls = "/message/"

class MessageNew(CreateView):
    model = Message
    fields = ['user', 'receipt', 'subject', 'content']
    success_url = reverse_lazy('msg_list')

class MessageDelete(DeleteView):
    model = Message
    success_urls = "/message/"

