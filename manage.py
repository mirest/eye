import os
from flask_script import manager
from flask_migrate import Migrate, MigrateCommnad
from app import db, create_aap
from app import models

app = create_aap(config_name=os.getenv('APP_SETTINGS'))
Migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommnad)

if __name__ == "__main__":
    manager.run
