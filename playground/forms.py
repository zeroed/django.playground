from django import forms

__author__ = 'eddie'


class RunTestTaskForm(forms.Form):
    name = forms.CharField(max_length=100, label='Task Name', required=False)
    number_of_tasks = forms.IntegerField(max_value=5, min_value=1, required=True)


class RunDetectorTaskForm(forms.Form):
    detector_name = forms.CharField(max_length=100, label='Detector Name', required=True)
