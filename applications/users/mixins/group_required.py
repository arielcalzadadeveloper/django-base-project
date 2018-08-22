from .user_check import UserCheckMixin


class GroupRequiredMixin(UserCheckMixin):
    def check(self, user):
        if getattr(self, 'group_required') is None:
            return True

        return user.is_authenticated and user.groups.filter(name=self.group_required).exists()

