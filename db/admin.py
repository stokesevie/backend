from django.contrib import admin
from .models import *

class dbAdmin(admin.ModelAdmin):
    pass

# Register your models here.

class courseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'level', 'start_date', 'end_date')

class tutorAdmin(admin.ModelAdmin):
    list_display=('username',)

class studentAdmin(admin.ModelAdmin):
    list_display=('username', 'level')

class student_enrollAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'lab_id')
class labAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'lab_id', 'date')
class axisAdmin(admin.ModelAdmin):
    list_display = ('x_id', 'y_id', 'x','y')
class axis_labelsAdmin(admin.ModelAdmin):
    list_display = ('pos_title', 'neg_title', 'risk', 'warn', 'avg')
class student_lab_riskAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'lab_id', 'axis_id', 'date', 'risk', 'warning', 'avg')
class messageAdmin(admin.ModelAdmin):
    list_display=('sender_id', 'receiver_id', 'sent_at', 'message_content')
class surveyAdmin(admin.ModelAdmin):
    list_display=('lab_id','question_1','question_2', 'question_3')
class questionAdmin(admin.ModelAdmin):
    list_display = ('x','y')

class responseAdmin(admin.ModelAdmin):
    list_display = ('x','y')

class student_surveyAdmin(admin.ModelAdmin):
    list_display = ('survey_id', 'student_id','response_1', 'response_2', 'response_3')

admin.site.register(student, studentAdmin)
admin.site.register(course, courseAdmin)
admin.site.register(tutor, tutorAdmin)
admin.site.register(db, dbAdmin)
admin.site.register(student_enroll,student_enrollAdmin)
admin.site.register(lab, labAdmin)
admin.site.register(axis_labels,axis_labelsAdmin)
admin.site.register(student_lab_risk,student_lab_riskAdmin)
admin.site.register(message, messageAdmin)
admin.site.register(survey, surveyAdmin)
admin.site.register(axis, axisAdmin)
admin.site.register(question,questionAdmin)
admin.site.register(response,responseAdmin)
admin.site.register(student_survey,student_surveyAdmin)