from django import forms

from todo.models import Tag, Task


class DateTimeInput(forms.DateTimeInput):
    """Class to allow not-text datetime input"""
    input_type = "datetime-local"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        widgets = {
            "deadline": DateTimeInput()
        }
        fields = "__all__"
