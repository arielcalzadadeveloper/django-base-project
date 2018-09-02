from django.views.generic import TemplateView

from applications.users.mixins.authenticated import AuthenticatedMixin


class ProfileCBV(AuthenticatedMixin, TemplateView):
    template_name = "users/profile.html"


Profile = ProfileCBV.as_view()
