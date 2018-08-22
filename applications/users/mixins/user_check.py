from django.core.exceptions import PermissionDenied # 403


class UserCheckMixin:
    def check(self, user):
        pass

    def failed(self, request, *args, **kwargs):
        raise PermissionDenied

    def dispatch(self, request, *args, **kwargs):
        if not self.check(request.user):
            return self.failed(request, *args, **kwargs)

        return super(UserCheckMixin, self).dispatch(request, *args, **kwargs)

