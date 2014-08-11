from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.assets import ManageAssets
from app import app, db
from app.ext.fixtures import FixtureCommand

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('assets', ManageAssets())
manager.add_command('db', MigrateCommand)
manager.add_command('fixture', FixtureCommand())

if __name__ == '__main__':
    manager.run()
