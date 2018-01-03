import os
import inspect
import sys
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mentor(db.Model):
    __tablename__ = "mentor"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    stack = db.Column(db.String(255))
    stack_details = db.Column(db.String(255))
    email = db.Column(db.String(255))
    slack_team = db.Column(db.String(255))
    blog = db.Column(db.String(255))
    gitprofile = db.Column(db.String(255))
    fbprofile = db.Column(db.String(255))
    linkedinprofile = db.Column(db.String(255))

    def __init__(self, full_name,
                 phone_number, stack, stack_details, email,
                 slack_team, blog, linkedin_profile=None,
                 git_profile=None, fb_profile=None):
        self.full_name = full_name
        self.contacts = phone_number
        self.stack = stack
        self.stack_details = stack_details
        self.email = email
        self.slack_team = slack_team
        self.blog = blog
        self.linkedinprofile = linkedin_profile
        self.gitprofile = git_profile
        self.fbprofile = fb_profile
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

        except:
            db.session.rollack()

    @staticmethod
    def get_all():
        return Mentor.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
