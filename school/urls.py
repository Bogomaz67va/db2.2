from django.urls import path
from school.views import Students

urlpatterns = [
    path('', Students.as_view(), name='students'),
]
