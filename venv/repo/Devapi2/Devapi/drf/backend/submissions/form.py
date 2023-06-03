from django.forms import ModelForm
from submissions.models import Submission
class SubmissionCreationForm(ModelForm):
    class Meta:
        model = Submission
        fields = ["submissionTitle", "submissionUpload"]