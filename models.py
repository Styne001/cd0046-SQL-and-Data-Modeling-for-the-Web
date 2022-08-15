from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Show(db.Model):
  __tablename__ = 'show'

  id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime, nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
  venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))

  def __repr__(self):
        return f'<Show {self.id} {self.start_time}>'
        


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.String(5))
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref=db.backref('Venue', lazy='joined', cascade='delete'))
    #shows = db.relationship('Show', secondary='details', backref=db.backref('Venue', lazy=True))

    def __repr__(self):
        return f'<Venue {self.name} {self.city} {self.state}'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.String(5))
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref=db.backref('Artist', lazy='joined', cascade='delete'))
    #shows = db.relationship('Show', secondary='details', backref='Artist', lazy=True)

    def __repr__(self):
        return f'<Artist {self.name} {self.city} {self.genres}'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.