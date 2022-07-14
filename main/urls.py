from django.urls import path
from .views import *

urlpatterns = [
    path('',Main2),
    path('home',Home),
    path('register/',Register),
    path('login/',Login),
    path('job/',Job),
    path('employee/',Employee),
    path('employee2/',Employee2),
    path('add-job/',AddJob),
    path('tahrir/',Tahrir),
    path('ochir/<int:id>/',Ochir),
    path('job2/',Job2),
    path('add-basejob/',BaseJobs),
    path('base-ochir/<int:id>/',BaseOchir),
    path('base-edit/<int:id>/',BaseEdit),
    path('filter2/',Filter2),
    path('filter/',Filter),
    path('add-worker/',AddWorker),
    path('add-worker1/',AddWorker1),




]
