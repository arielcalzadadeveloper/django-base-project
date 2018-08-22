from crispy_forms.helper import FormHelper
from crispy_forms.helper import Layout
from crispy_forms.layout import Div
from crispy_forms.layout import HTML
from crispy_forms.bootstrap import PrependedText


class BaseLayout(FormHelper):
    def __init__(self, *args, **kwargs):
        super(BaseLayout, self).__init__(*args, **kwargs)

        self.layout = Layout()
        self.form_class = ""
        self.form_action = "#"

    @staticmethod
    def make_row(elements, size=None):
        cols = []

        for element in elements:
            cols.append(Div(
                element,
                css_class="col{}".format("-{}".format(size) if size else "")
            ))

        return Div(
            *cols,
            css_class="row"
        )

    def make_empty_row(self):
        self.layout.fields.append(self.make_row([HTML("<br>")]))

    def make_hr_row(self):
        self.layout.fields.append(self.make_row([HTML("<br><hr><br>")]))

    def money_field(self, field_name):
        field = PrependedText(
            field_name,
            "$"
        )

        return field

    def make_right_buttons(self, buttons):
        self.layout.fields.append(Div(
            *buttons,
            css_class="text-right"

        ))

    @staticmethod
    def make_button(label="Enviar", css_class="btn-primary", awesome_icon=None, button_type="submit"):
        icon = "<i class='{}'></i>".format(awesome_icon) if awesome_icon else ""

        return HTML(
            """
            <button class="btn {css_class}" type="{button_type}">
                {icon}
                {label}
            </button>
            """.format(label=label, css_class=css_class, icon=icon, button_type=button_type)
        )

    @staticmethod
    def make_href_button(href="#", label="Enviar", css_class="btn-primary", awesome_icon=None, title=""):
        icon = "<i class='{}'></i>".format(awesome_icon) if awesome_icon else ""

        return HTML("""
            <a href="{href}" class="btn {css_class}" title="{title}">
                {icon}
                {label}
            </a>
            """.format(label=label, css_class=css_class, icon=icon, href=href, title=title)
        )
