from flask.ext.script import Command, Manager

from main import app, db
import requests
import json
import datetime
from models.event import Event, EventFavourite
from models.user import User

manager = Manager(app)

class Notify(Command):
    def run(self):
        app.logger.info("Checking for events starting in the next 10 minutes (%s - %s)" % (datetime.datetime.strftime(datetime.datetime.now()+datetime.timedelta(minutes=5), "%Y-%m-%dT%H:%M:%SZ"), datetime.datetime.strftime(datetime.datetime.now()+datetime.timedelta(minutes = 10), "%Y-%m-%dT%H:%M:%SZ")))
        events = db.session.query(Event).filter(Event.start_time.between(datetime.datetime.strftime(datetime.datetime.now()+datetime.timedelta(minutes=5), "%Y-%m-%dT%H:%M:%SZ"), datetime.datetime.strftime(datetime.datetime.now()+ datetime.timedelta(minutes = 10), "%Y-%m-%dT%H:%M:%SZ")))
        for i in events:
            for usr in db.session.query(EventFavourite).filter(EventFavourite.event_id==i.id):
                db.session.query(User).filter(User.id == usr.user_id).first().notify("Your talk '%s' is starting soon (%s)" % (i.title, datetime.datetime.strftime(i.start_time, "%H:%M")))

        app.logger.info("All done")

if __name__ == "__main__":
  manager.add_command('notify', Notify())
  manager.run()