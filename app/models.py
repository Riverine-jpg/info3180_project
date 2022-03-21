from . import db

class Properties(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    ptitle = db.Column(db.String(80))
    desc = db.Column(db.String(512))
    rooms = db.Column(db.Integer())
    brooms = db.Column(db.Integer())
    price = db.Column(db.Float())
    ptype = db.Column(db.String(64))
    locat = db.Column(db.String(128))
    photo = db.Column(db.String(128))

    def __init__(self, ptitle, desc, rooms, brooms, price, ptype, locat, photo):
            self.ptitle = ptitle
            self.desc = desc
            self.rooms = rooms
            self.brooms = brooms
            self.price = price
            self.ptype = ptype
            self.locat = locat
            self.photo = photo


    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.ptitle)
