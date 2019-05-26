import os


def override_settings(settings):
    settings.BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    settings.APPS = (
        "staff"
    )
