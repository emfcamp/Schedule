#!/usr/bin/env python

from flask.ext.script import Command, Manager

from main import app, db


manager = Manager(app)

class CreateDB(Command):
    def run(self):
        db.create_all()


if __name__ == "__main__":
  manager.add_command('createdb', CreateDB())
  manager.run()

