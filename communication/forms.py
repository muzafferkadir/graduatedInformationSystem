from django import forms
from django.utils.translation import gettext_lazy as _


class MessageForm(forms.Form):
    message = forms.CharField(max_length=140, label=_("Message"))
    file = forms.FileField(required=False, label=_("File"))
