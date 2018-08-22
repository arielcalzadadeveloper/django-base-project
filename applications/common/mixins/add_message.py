from django.contrib import messages
from django.utils.timezone import now
from django.utils.timezone import localtime


class AddMessageMixin(object):
    def add_success_message(self, with_datetime=False):
        msg = u"Operación realizada exitosamente"

        if with_datetime:
            msg = u"{} {}".format(
                msg,
                localtime(now()).strftime("%Y-%m-%d %H:%M:%S")
            )

        messages.add_message(
            self.request,
            messages.SUCCESS,
            msg
        )

    def add_error_message(self, msg=None):
        if not msg:
            msg = u"La información diligenciada requiere algunas correcciones"

        messages.add_message(
            self.request,
            messages.ERROR,
            msg
        )

    def form_valid(self, form):
        self.add_success_message()

        return super(AddMessageMixin, self).form_valid(form)

    def form_invalid(self, form):
        self.add_error_message()

        return super(AddMessageMixin, self).form_invalid(form)

    def formset_valid(self, form):
        self.add_success_message()

        return super(AddMessageMixin, self).formset_valid(form)

    def formset_invalid(self, form):
        self.add_error_message()

        return super(AddMessageMixin, self).formset_invalid(form)

    def forms_valid(self, form, inlines):
        self.add_success_message()

        return super(AddMessageMixin, self).forms_valid(form, inlines)

    def forms_invalid(self, form, inlines):
        self.add_error_message()

        return super(AddMessageMixin, self).forms_invalid(form, inlines)
