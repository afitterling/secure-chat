from extensions import db
from builtins import classmethod

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True, unique=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()


#    def serialize(self):
#        return {"id": self.id, "title": self.name }

