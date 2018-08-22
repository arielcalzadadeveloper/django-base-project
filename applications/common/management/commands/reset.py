import os

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        database_settings = settings.DATABASES.get("default")

        name = database_settings.get("NAME")
        user = database_settings.get("USER")
        password = database_settings.get("PASSWORD")

        export_cmd = "export PGPASSWORD=\"{password}\"".format(password=password)
        drop_cmd = "dropdb {name} -U {user} --if-exists".format(name=name, user=user)
        encoding_options = "--encoding=\"utf-8\" --locale=en_US.utf8 --template=template0"
        create_cmd = "createdb {name} -U {user} {encoding_options}".format(name=name,
                                                                           user=user,
                                                                           encoding_options=encoding_options)
        cmd = "{export_cmd} && {drop_cmd} && {create_cmd}".format(export_cmd=export_cmd,
                                                                  drop_cmd=drop_cmd,
                                                                  create_cmd=create_cmd)

        os.system(cmd)

        call_command("migrations")
