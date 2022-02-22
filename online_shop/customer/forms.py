from django import forms
from django.utils.translation import gettext_lazy as _

from customer.models import Customer
from core.models import User
from core.validators import check_phone


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
        fields = ["phone", "password"]

        labels = {
            'phone': _("Phone Number"),
            'password': _("Password"),
        }

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': _("Example: 09123456789")}),
            'password': forms.PasswordInput(),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        return check_phone(phone)
