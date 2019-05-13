from django.urls import include, path

from .views import UserListView, UserCreate

app_name = 'accounts'

urlpatterns = [
    path('', UserListView.as_view()),
    path('register/', UserCreate.as_view()),
]