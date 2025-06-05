from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, validators
from wtforms.validators import DataRequired, Email, Length

class EnrollmentForm(FlaskForm):
    name = StringField('Full Name', [
        DataRequired(message='Name is required'),
        Length(min=2, max=100, message='Name must be between 2 and 100 characters')
    ])
    
    email = StringField('Email Address', [
        DataRequired(message='Email is required'),
        Email(message='Please enter a valid email address')
    ])
    
    phone = StringField('Phone Number', [
        DataRequired(message='Phone number is required'),
        Length(min=10, max=15, message='Please enter a valid phone number')
    ])
    
    course_interested = SelectField('Course Interested', [
        DataRequired(message='Please select a course')
    ], choices=[
        ('', 'Select a Course'),
        ('corporate_accountant', 'Corporate Accountant Training'),
        ('basic_accounting', 'Basic Accounting'),
        ('advanced_accounting', 'Advanced Accounting'),
        ('stock_market_basics', 'Stock Market Basics'),
        ('technical_analysis', 'Technical Analysis'),
        ('fundamental_analysis', 'Fundamental Analysis'),
        ('trading_strategies', 'Trading Strategies'),
        ('python_programming', 'Python Programming'),
        ('web_development', 'Web Development'),
        ('data_science', 'Data Science'),
        ('digital_marketing', 'Digital Marketing'),
        ('devops', 'DevOps Engineering'),
        ('aws_cloud', 'AWS Cloud Computing')
    ])
    
    message = TextAreaField('Additional Message', [
        Length(max=500, message='Message cannot exceed 500 characters')
    ])

class ContactForm(FlaskForm):
    name = StringField('Full Name', [
        DataRequired(message='Name is required'),
        Length(min=2, max=100, message='Name must be between 2 and 100 characters')
    ])
    
    email = StringField('Email Address', [
        DataRequired(message='Email is required'),
        Email(message='Please enter a valid email address')
    ])
    
    subject = StringField('Subject', [
        DataRequired(message='Subject is required'),
        Length(min=5, max=200, message='Subject must be between 5 and 200 characters')
    ])
    
    message = TextAreaField('Message', [
        DataRequired(message='Message is required'),
        Length(min=10, max=1000, message='Message must be between 10 and 1000 characters')
    ])
