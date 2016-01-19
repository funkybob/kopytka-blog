from django import forms

from . import models


class PostAdminForm(forms.ModelForm):
    auto = forms.BooleanField(label='Auto-tag?', required=False, initial=True,
                              help_text="Automatically scan content for tags")

    class Meta:
        model = models.Post
        exclude = ('posted_by',)
