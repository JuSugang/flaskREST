from api import db
from sqlalchemy.dialects.postgresql import JSON

class Result(db.Model):
    __tablename__ = 'particle_table'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String())
    particles = db.Column(db.String())

    def __init__(self,timestamp, particles):
        self.timestamp = timestamp
        self.particles = particles

    def __repr__(self):
        return '<id {}>'.format(self.id)