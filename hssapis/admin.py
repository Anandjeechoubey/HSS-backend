from django.contrib import admin

# Register your models here.
from .models import Faculty, Student, Office_staff, Announcement, Award, News, Phd_awarded, CommitteePerson, Project, Past_Talk, Special_Talk, Conf_Work_Pres

admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Office_staff)
admin.site.register(Announcement)
admin.site.register(Award)
admin.site.register(News)
admin.site.register(Phd_awarded)
admin.site.register(CommitteePerson)
admin.site.register(Project)
admin.site.register(Past_Talk)
admin.site.register(Special_Talk)
admin.site.register(Conf_Work_Pres)