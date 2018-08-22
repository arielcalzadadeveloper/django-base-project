import os
import uuid


def get_current_application(request):
    """Get current application."""
    try:
        app_name = request.resolver_match.namespace

        if not app_name:
            app_name = "home"
    except Exception as e:
        app_name = "home"

    return app_name


def generate_file_name(file_name):
    """Create a generic file name."""
    name = uuid.uuid4().hex
    _, extension = os.path.splitext(file_name)

    return "{}{}".format(name, extension)
