from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Message 

# Create your views here.
class MessageList(ListView):
    model = Message


class MessageRead(DetailView):
    model = Message

