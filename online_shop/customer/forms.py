from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

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


class UserForm(forms.ModelForm):  # TODO: add re-enter password
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = User
        # fields = "__all__"
        fields = ["phone", "password"]

        labels = {
            'phone': _("Phone Number"),
            'password': _("Password"),
            'password2': _("Confirm Password"),
        }

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': _("Example: 09123456789")}),
            'password': forms.PasswordInput(),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        return check_phone(phone)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] and cd["password2"] and cd["password"] != cd["password2"]:
            raise ValidationError(_("Passwords does not match."))
        return cd["password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "email"]

        labels = {
            'first_name': _("First Name"),
            'last_name': _("Last Name"),
            'phone': _("Phone Number"),
            'email': _("Email"),
        }


class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        labels = {
            'new_password': _("New Password"),
        }