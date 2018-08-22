from django.contrib import admin


class DisableDeleteAdminMixin:
    """Mixin for disabling delete."""
    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(DisableDeleteAdminMixin, self).get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]

        return actions


class DisableAddAdminMixin:
    """Mixin for disabling add."""
    def has_add_permission(self, request, obj=None):
        return False


class BaseAdminMixin(admin.ModelAdmin):
    pass
