from backstack.app import create_app

from base.config import override_settings


app = create_app(override_settings=override_settings)