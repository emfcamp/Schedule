from flask.ext.script import Command, Manager

from main import app, db
import requests
import json
import datetime
from models.event import Event

manager = Manager(app)

class ImportSchedule(Command):
    def run(self):
        app.logger.info("Updating schedule")

        resp = requests.get(url=app.config['SCHEDULE_URL'])
        schedule_json = json.loads(resp.text);

        for event_data in schedule_json['conference_events']['events']:
            event = db.session.query(Event).filter_by(id=event_data['id']).first()
            if event:
                event_does_not_exist_yet = False
                event.title = event_data['title']
                event.type = event_data['type']
            else:
                event_does_not_exist_yet = True
                event = Event(event_data['id'], event_data['title'], event_data['type'])

            event.abstract = event_data['abstract']

            if 'room' in event_data:
                #TODO: notify on talk ID changing
                event.location_name = event_data['room']['name']
                event.location_id = event_data['room']['id']
            else:
                event.location_name = None
                event.location_id = None

            if 'start_time' in event_data:
                #TODO: notify on talk time changing
                event.start_time = datetime.datetime.strptime(event_data['start_time'], "%Y-%m-%dT%H:%M:%SZ")
                event.end_time = datetime.datetime.strptime(event_data['end_time'], "%Y-%m-%dT%H:%M:%SZ")
            else:
                event.start_time = None
                event.end_time = None

            speaker_names = []
            for speaker in event_data['speakers']:
                speaker_names.append(speaker['full_public_name'])
            event.speaker_names = ", ".join(speaker_names)

            if event_does_not_exist_yet:
                db.session.add(event)
            db.session.commit()


        app.logger.info("All done")

if __name__ == "__main__":
  manager.add_command('import_schedule', ImportSchedule())
  manager.run()