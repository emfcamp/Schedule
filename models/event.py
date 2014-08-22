from main import db
import pprint

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    type_id = db.Column(db.String, nullable=False)

    abstract = db.Column(db.String, nullable=True)
    speaker_names = db.Column(db.String, nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    location_id = db.Column(db.Integer, nullable=True)
    location_name = db.Column(db.String, nullable=True)

    def __init__(self, id, title, type_id):
        self.id = id
        self.title = title
        self.type_id = type_id

    def matches_day(self, day_of_month):
        if day_of_month == 0:
            return self.start_time == None
        else:
            if not self.start_time:
                return False
            return int(self.start_time.strftime('%d')) == day_of_month



