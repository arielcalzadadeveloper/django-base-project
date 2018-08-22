from django.views.generic import TemplateView


class HomeCBV(TemplateView):
    template_name = "users/home.html"


Home = HomeCBV.as_view()
