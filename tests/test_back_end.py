import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Users, Posts
#from flask import Flask
#from flask.ext.bcrypt import Bcrypt

#app = Flask(__name__)
#bcrypt = Bcrypt(app)

class TestBase(TestCase): 

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
       # app.config.update(
        #    SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASS'))+'@'+str(getenv('MYSQL_URL'))+'/'+str(getenv('MYSQL_DB_TEST'))        )
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASS'))+'@'+str(getenv('MYSQL_URL'))+'/'+str(getenv('MYSQL_DB_TEST'))        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = Users(first_name='admin', last_name='admin',email="admin@admin.com", password="admin2016")


        # create test non-admin user
        employee = Users(first_name='test', last_name='test',email="test@user.com", password="test2016")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

class testingtesting(TestBase):
    
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_user_view(self):
        target_url = url_for('account')
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)

    def test_add_update_delete(self):
        post = Posts(englishh="yes", spanishh="si", comment="n/a")
        db.session.add(post)
        db.session.commit()

        self.assertEqual(Posts.query.count(), 1)
    def test_update_account(self):
        user = Users(first_name="lucy", last_name="lu", email="lucylu@gmail.com", password="lucylu")
        db.session.add(user)
        db.session.commit()
        user = Users(first_name="simon", last_name="chen", email="simon@gmail.com", password="simon")
        db.session.commit()

        self.assertEqual(Users.query.count(), 3)

    def test_delete_account(self):
        user = Users(first_name="simon", last_name="chen", email="simon@gmail.com", password="simon")
        db.session.add(user)
        db.session.commit()

        db.session.delete(user)
        db.session.commit()

        self.assertEqual(Users.query.count(), 2)




        
        



