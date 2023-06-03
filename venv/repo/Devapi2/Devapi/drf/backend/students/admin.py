from django.contrib import admin
from forum.models import Forum
from assignments.models import Assignment
from students.models import Student
from comments.models import Comment
from submissions.models import Submission
# Register your models here.

admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Forum)
admin.site.register(Comment)
admin.site.register(Submission)
