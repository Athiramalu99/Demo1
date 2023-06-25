from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cvbhome', views.Tasklistview.as_view(), name='cbvhome'),
    path('cvbdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cvbdetail'),
    path('cvbupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cvbupdate'),
    path('cvbdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cvbdelete')

    # path('details', views.details, name='details')
]
