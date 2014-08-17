from main import db

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    type_id = db.Column(db.Integer, nullable=False)

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


