import os.path

from django.apps import AppConfig, apps

from .oso import Oso

class DjangoOsoConfig(AppConfig):
    name = 'django_oso'

    def ready(self):
        # Load all polar files in each app's "policy" directory.
        for app in apps.get_app_configs():
            policy_dir = os.path.join(app.path, 'policy')
            for path, _, filenames in os.walk(policy_dir):
                for file in filenames:
                    path = os.path.join(path, file)
                    if os.path.splitext(file)[1] == '.polar':
                        Oso.load_file(path)

        # TODO (dhatch): Provide setting to disable auto loading
        # customize file directory
        # customize policy files
        # document how to do manual load.


        # Register all models

        # ?? NAMESPACING ??


        # TODO (dhatch): Provide setting to disable model registration.
