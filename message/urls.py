from django.urls import path
from . import views

urlpatterns = [
    # massage/ => 留言列表
    path('', views.MessageList.as_view(), name='msg_list'),
    path('<int:pk>/', views.MessageRead.as_view(), name="msg_read"),
    path('create', views.MessageNew.as_view(), name='msg_create'),
     path('<int:pk>/delete', views.MessageDelete.as_view(), name="msg_delete"),
]