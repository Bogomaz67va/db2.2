from django.views.generic import ListView

from .models import Student


class Students(ListView):
    model = Student
    template_name = 'school/students_list.html'
    ordering = 'group'
    queryset = Student.objects.prefetch_related('teacher').order_by(ordering)

