from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class User(UserMixin, db.Model):
    """
    User class to define user objects
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blogs = db.relationship("Blog", backref="user", lazy="dynamic")
    comment = db.relationship("Comment", backref="user", lazy="dynamic")
    like = db.relationship("Like", backref="user", lazy="dynamic")
    dislike = db.relationship("Dislike", backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User {self.username}"