from django.forms import ModelForm
from assignments.models import Assignment
class AssignmentCreationForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ["assignmentTitle", "assignmentUpload"]