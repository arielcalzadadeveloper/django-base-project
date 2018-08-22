from django.conf.urls import url

from applications.users.views.home import Home

app_name = "users"

urlpatterns = [
    url(regex=r"^$", view=Home, name="home"),
]
