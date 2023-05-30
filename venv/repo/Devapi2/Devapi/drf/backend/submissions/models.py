from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


import magic
ext_validator = FileExtensionValidator(['jpg', 'png', 'text', 'pdf'])

def validate_file_mimetype(file):
    accept = ['application/msword', 'text/plain', 'application/pdf', 'image/jpeg', 'image/png']
    fileMimeType = magic.from_buffer(file.read(1024), mime=True)
    print(fileMimeType)
    if fileMimeType not in accept:
        raise ValidationError("Unsupported file type")

# Create your models here.
class Submission(models.Model):
    submissionUpload = models.FileField(upload_to="uploads/%Y/%m/%d/", validators=[ext_validator, validate_file_mimetype])
    students = models.ManyToManyField(User)