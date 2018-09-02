class AddRequestToFormMixin(object):
    def get_form_kwargs(self):
        kwargs = super(AddRequestToFormMixin, self).get_form_kwargs()
        kwargs.update({
            'request': self.request,
        })

        return kwargs

