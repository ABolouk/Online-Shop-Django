from django import forms
from django.utils.translation import gettext_lazy as _

from core.models import User


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["phone", "password"]
#
#         labels = {
#             'phone': _("Phone Number"),
#             'password': _("Password"),
#         }
#
#         widgets = {
#             'phone': forms.TextInput(attrs={'placeholder': _("Example: 09123456789")}),
#             'password': forms.PasswordInput(),
#         }


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=15, label=_("Phone"))
    password = forms.CharField(max_length=100, label=_("Password"), widget=forms.PasswordInput)
