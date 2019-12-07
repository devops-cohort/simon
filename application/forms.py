from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users
from flask_login import LoginManager, current_user


class PostForm(FlaskForm):
    englishh = StringField('English',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    spanishh = StringField('Spanish',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    comment = StringField('Comment',
            validators = [
                Length(min=0, max=100)
            ]
    )

    author = StringField('Author',
            validators = [
                Length(min=0, max=100)
            ]
    )

    submit = SubmitField('Submit translation')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )
    
    email = StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
    )
    
    password = PasswordField('Password', 
            validators=[
                DataRequired()
            ]
    )
    
    confirm_password = PasswordField('Confirm Password',
            validators=[
                DataRequired(),
                EqualTo('password')
            ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        
        if user:
            raise ValidationError('Email is already in use!')


class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
	]
    )   

    password = PasswordField('Password',
        validators=[
	    DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    email = StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
    )
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('Email is already in use!')
    
    submit = SubmitField('Update account')


class UpdateTableForm(FlaskForm):
    englishh = StringField('English',
            validators = [
                DataRequired(),
                Length(min=1, max=30)
            ]
    )

    spanishh = StringField('Spanish',
            validators = [
                DataRequired(),
                Length(min=1, max=30)
            ]
    )

    comment = StringField('Comment',
            validators=[
                Length(min=0, max=30)
            ]
    )

    submit = SubmitField('Update table')

class DeleteForm(FlaskForm):
    delete = BooleanField('Delete table')
    submit = SubmitField('Confirm delete')
