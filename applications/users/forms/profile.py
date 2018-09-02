from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if email and self.request.user.email != email and User.objects.filter(email=email).exists():
                raise forms.ValidationError("Correo electrónico existente")

        return email

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
