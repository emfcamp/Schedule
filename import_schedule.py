from flask.ext.script import Command, Manager

from main import app, db
import requests
import json
from models.event import Event

manager = Manager(app)

class ImportSchedule(Command):
    def run(self):
        app.logger.info("Updating schedule")

        resp = requests.get(url=app.config['SCHEDULE_URL'])
        schedule_json = json.loads(resp.text);

        for event_data in schedule_json['conference_events']['events']:
            event = Event(event_data['id'], event_data['title'], event_data['type'])

            speaker_names = []
            for speaker in event_data['speakers']:
                speaker_names.append(speaker['full_public_name'])
            event.speaker_names = ", ".join(speaker_names)
            print event.speaker_names
            # ToDo: Add start, end and location
            db.session.add(event)

        db.session.commit()

        app.logger.info("All done")

if __name__ == "__main__":
  manager.add_command('import_schedule', ImportSchedule())
  manager.run()