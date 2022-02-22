from django import forms
from django.utils.translation import gettext_lazy as _

from customer.models import Customer
from core.models import User


class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user', ]

        labels = {
            'first_name': _("First Name"),
            'last_name': _("Last Name"),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ["username", "phone"]

        labels = {
            'phone': _("Phone Number"),
            'password': _("Password"),
        }

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': _("Example: 09132985527")}),
            'password': forms.PasswordInput(),
        }
