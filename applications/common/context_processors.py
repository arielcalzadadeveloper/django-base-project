from django.conf import settings

from applications.common import utilities


def current_application(request):
    return dict(CURRENT_APPLICATION=utilities.get_current_application(request),
                BROWSER_WINDOW_TITLE=settings.BROWSER_WINDOW_TITLE,
                BASE_TEMPLATE_HEADER=settings.BASE_TEMPLATE_HEADER)
