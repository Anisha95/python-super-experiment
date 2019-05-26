#!/usr/bin/env python
from migrate.versioning.shell import main
from backstack.config import settings


if __name__ == '__main__':
    main(repository='db-migrations', url=settings.DB_DEFAULT, debug='False')
