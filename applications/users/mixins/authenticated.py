from django.shortcuts import redirect


class AuthenticatedMixin:
    def check(self, user):
        return user.is_authenticated

    def failed(self, request, *args, **kwargs):
        return redirect("account_login")

    def dispatch(self, request, *args, **kwargs):
        if not self.check(request.user):
            return self.failed(request, *args, **kwargs)

        return super(AuthenticatedMixin, self).dispatch(request, *args, **kwargs)
