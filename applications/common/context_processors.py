from django.conf import settings

from applications.common import utilities


def general(request):
    return dict(CURRENT_APPLICATION=utilities.get_current_application(request),
                BROWSER_WINDOW_TITLE=settings.BROWSER_WINDOW_TITLE)
