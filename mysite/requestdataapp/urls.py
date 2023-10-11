from django.urls import path
from .views import user_info, params, file_upload

app_name = 'requestdataapp'

urlpatterns = [
    path('user-info/', user_info, name="user"),
    path('get/', params, name="get"),
    path('file/', file_upload, name="file_upload"),

]
