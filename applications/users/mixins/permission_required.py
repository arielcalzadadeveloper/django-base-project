from .user_check import UserCheckMixin


class PermissionRequiredMixin(UserCheckMixin):
    def check(self, user):
        if getattr(self, 'permission_required') is None:
            return True

        return user.is_authenticated and user.has_perm(self.permission_required)

