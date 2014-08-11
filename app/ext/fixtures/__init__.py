import importlib
import os

from flask.ext.script import Command, Option


class FixtureCommand(Command):
    option_list = (
        Option('--fixture', '-f', dest='fixture_path',
               help='Path to the fixture you want to install.', required=True),
        Option('--dry-run', dest='dry_run', help='Disables commit if set.',
               action='store_true', default=False)
    )

    def run(self, fixture_path, dry_run):
        fixture_module_name = fixture_path.replace(os.sep, '.').strip('.')[:-3]
        fixture_module = importlib.import_module(fixture_module_name)
        try:
            fixture_module.install(dry_run)
        except Exception, err:
            raise err('Fixture is required to implement an install function.')
