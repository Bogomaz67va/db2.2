from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # data = list()
    ordering = 'group'
    data = Student.objects.prefetch_related('teacher').order_by(ordering)
    # for student in group:
    #     for teacher in student.teacher.all():
    #         data.append({
    #             student: teacher,
    #         })
    #         print(f"{student.name} - {student.group} - {teacher.name} - {teacher.subject}")
    # return HttpResponse(data)
    context = {'object_list': data}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
