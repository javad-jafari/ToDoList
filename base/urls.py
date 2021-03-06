
from django.urls import path
from base.views import RegistrePage, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks' ),
    path('login/', CustomLoginView.as_view(), name='login' ),
    path('register/', RegistrePage.as_view(), name='register' ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout' ),
    path('task/<int:pk>/', TaskDetail.as_view(), name='taskdetail' ),
    path('task-create', TaskCreate.as_view(), name='task-create' ),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update' ),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete' ),


    ]