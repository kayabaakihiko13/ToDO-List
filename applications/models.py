from applications import db

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    status=db.Column(db.Boolean)
    
    
    def __str__(self):
        return self.id


