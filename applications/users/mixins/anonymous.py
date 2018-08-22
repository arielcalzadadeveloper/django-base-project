from .user_check import UserCheckMixin


class AnonymousMixin(UserCheckMixin):
    def check(self, user):
        return user.is_anonymous
