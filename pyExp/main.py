from backstack import Commands
from backstack.app import create_app

from Base.config import override_settings

if __name__ == '__main__':
    commands = Commands(app=create_app(override_settings=override_settings))
    commands.execute()
