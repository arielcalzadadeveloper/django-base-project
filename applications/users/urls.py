from django.conf.urls import url

from applications.users.views.profile import Profile

app_name = "users"

urlpatterns = [
    url(regex=r"^$", view=Profile, name="profile"),
]
