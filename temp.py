
from app.models import Properties
from app import db
Properties.query.filter_by(id=5).delete()
db.session.commit()