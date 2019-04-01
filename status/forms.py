from django import forms
from status.models import Status


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = [
            'user',
            'summary',
            'image'
        ]

    def clean_content(self, *args, **kwargs):
        summary = self.cleaned_data.get('summary')
        if len(summary) > 240:
            raise forms.ValidationError("Content is too long")
        return summary

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        summary = data.get('summary', None)

        if summary == "":
            summary = None

        image = data.get("image", None)
        if (summary is None) and (image is None):
            raise forms.ValidationError('Content or image is required.')

        return super().clean(*args, **kwargs)
