from .user_check import UserCheckMixin


class SuperuserMixin(UserCheckMixin):
    def check(self, user):
        return user.is_superuser

