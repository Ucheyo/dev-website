from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

import magic
ext_validator = FileExtensionValidator(['jpg', 'png', 'txt', 'pdf'])

def validate_file_mimetype(file):
    accept = ['application/msword', 'text/plain', 'application/pdf', 'image/jpeg', 'image/png']
    fileMimeType = magic.from_buffer(file.read(1024), mime=True)
    print(fileMimeType)
    if fileMimeType not in accept:
        raise ValidationError("Unsupported file type")
# Create your models here.
class Assignment(models.Model):
    assignmentTitle = models.TextField(max_length=100, blank=True, default='')
    assignmentUpload = models.FileField(upload_to="assignemnts/%Y/%m/", validators=[ext_validator, validate_file_mimetype])  
