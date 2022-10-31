from players import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    location = db.Column(db.DateTime())
    players = db.relationship('Player', backref='owner')


    def __repr__(self):
        return f'Team{self.name}{self.location}'

class Player(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    team_on = db.Column(db.Integer,db.ForeignKey('team.id'))

    def __repr__(self):
        return f'Player{self.first_name}{self.last_name}'
