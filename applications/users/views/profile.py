from django.shortcuts import reverse
from django.views.generic import UpdateView

from applications.users.forms.profile import ProfileForm
from applications.users.layouts.profile import ProfileLayout
from applications.users.mixins.authenticated import AuthenticatedMixin
from applications.common.mixins.add_message import AddMessageMixin
from applications.common.mixins.add_request_to_form import AddRequestToFormMixin


class ProfileCBV(AddRequestToFormMixin, AddMessageMixin, AuthenticatedMixin, UpdateView):
    template_name = "users/profile.html"
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super(ProfileCBV, self).get_context_data(**kwargs)

        context_data.update({
            "form_layout": ProfileLayout(),
        })

        return context_data

    def get_success_url(self):
        return reverse("users:profile")


Profile = ProfileCBV.as_view()
