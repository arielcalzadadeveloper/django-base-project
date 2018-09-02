from django.shortcuts import reverse

from applications.common.layouts.base import BaseLayout


class ProfileLayout(BaseLayout):
    def __init__(self, *args, **kwargs):
        super(ProfileLayout, self).__init__(*args, **kwargs)

        self.form_action = reverse("users:profile")
        self.make_layout()

    def make_layout(self):
        self.layout.fields.append(
            self.make_row([
                "first_name",
            ])
        )

        self.layout.fields.append(
            self.make_row([
                "last_name",
            ])
        )

        self.layout.fields.append(
            self.make_row([
                "email",
            ])
        )

        self.make_hr_row()

        self.make_right_buttons([
            self.make_button(label="Guardar", awesome_icon="fas fa-plus", css_class="btn-success"),
        ])
