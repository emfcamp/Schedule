from main import db
import pprint
import datetime

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

    def in_the_past(self):
        if self.end_time:
            return self.end_time < datetime.datetime.now()
        else:
            return False

    def happening_now(self):
        if self.start_time and self.end_time:
            return self.start_time < datetime.datetime.now() < self.end_time
        else:
            return False

    def matches_day(self, day_of_month):
        if day_of_month == 0:
            return self.start_time == None
        else:
            if not self.start_time:
                return False
            return int(self.start_time.strftime('%d')) == day_of_month

    def is_scheduled(self):
        return day_of_month != 0

    def day_name(self):
        if self.start_time is None:
            return "All days or not yet scheduled"
        else:
            return self.start_time.strftime('%A')

    @staticmethod
    def group_events_by_date(events):
        days = {}
        for event in events:
            if event.start_time is not None:
                if event.start_time.date() in days:
                    days[event.start_time.date()].append(event)
                else:
                    days[event.start_time.date()] = [event]
            elif None in days:
                days[None].append(event)
            else:
                days[None] = [event]
        return days


class EventFavourite(db.Model):
    __tablename__ = 'event_favourite'
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    user = db.relationship("User", backref="event_favourites")
    event = db.relationship("Event")

    def __init__(self, event=None, user=None):
        self.event = event
        self.user = user
