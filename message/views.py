from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Message
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class MessageList(ListView):
    model = Message

    ordering = ['created', 'id']
    #message/mesage_list.html
    #頁面範本檔案名稱應用程式/資料模型_.html => message/message_list.html
    #頁面範本變數名稱資料模型_list => message_list

class MessageRead(DetailView):
    model = Message

        #頁面範本檔案名稱應用程式/資料模型_detail.html => message/message_detail.html
        #頁面範本變數名稱資料模型_list => message
class MessageNew(CreateView):
    model = Message
    fields = ['user', 'receipt', 'subject', 'content']
    
    success_url = reverse_lazy('msg_list') 
    # field = '__all__'
    #頁面範本檔案名稱:應用程式/資料模型_form.html => message/message_detail.html
    #頁面範本變數名稱:form


class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = '/message/'

        #頁面範本檔案名稱:應用程式/資料模型_confirm_delete.html => message/message_confirm_delete.html
        #頁面範本變數名稱:form, object, 資料模型(小寫)

