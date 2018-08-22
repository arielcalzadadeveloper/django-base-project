from .user_check import UserCheckMixin


class PermissionsORRequiredMixin(UserCheckMixin):
    def check(self, user):
        if self.permissions_required is None:
            return True

        if not user.is_authenticated:
            return False

        for permission_required in self.permissions_required:
            if user.has_perm(permission_required):
                return True

        return False

