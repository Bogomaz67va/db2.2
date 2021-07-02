from django.contrib import admin
from .models import Student, Teacher, Groups


class GroupShipInline(admin.TabularInline):
    model = Groups


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [GroupShipInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [GroupShipInline]
