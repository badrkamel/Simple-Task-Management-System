from django.urls import path, include
from rest_framework import routers
from tasks import views

app_name = 'tasks'

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register('', views.TaskView, 'tasks')

# The API URLs are now determined automatically by the router.
urlpatterns = [


    path('tasks/', include(router.urls)),

    path('me/all/', views.my_tasks, name='my-tasks'),
    path('me/<int:pk>/', views.task_detail, name='task-detail'),

    path('me/completed/', views.tasks_completed, name='compleated'),
    path('me/incompleted/', views.tasks_incompleted, name='incompleated'),

    # Export data.
    path('export/csv/', views.save_as_csv, name='save-as-csv'),
    path('export/xls/', views.save_as_xls, name='save-as-xls')

]