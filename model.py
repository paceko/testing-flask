from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    g1 = Game(name="Ticket to Ride", description="a cross-country train adventure")
    g2 = Game(name="Power Grid", description="supply the most cities with power")
    g3 = Game(name="Amazing Labyrinth", description="move around the shifting paths of the labyrinth in a race to collect various treasures")


    db.session.add_all([g1, g2, g3])
    db.session.commit()




if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print "Connected to DB."
 