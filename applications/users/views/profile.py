from django.views.generic import TemplateView


class ProfileCBV(TemplateView):
    template_name = "users/profile.html"


Profile = ProfileCBV.as_view()
