from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('board/<int:pk>', views.BoardDetail.as_view(), name='detailBoard'),
    path('new', views.newBoard, name='newBoard'),
    path('board/<int:boardId>/delete', views.BoardDelete, name='BoardDelete'),
    path('board/<int:pk>/comment/new', views.CommentCreate, name='CommentCreate'),
]
