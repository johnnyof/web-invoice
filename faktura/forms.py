from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from faktura.models import Customer


class CustomerRegistration(FlaskForm):
    first_name = StringField('First name', validators=[
                             DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last name', validators=[
                            DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    phone_number = IntegerField('phone number', validators=[DataRequired()])
    submit = SubmitField('Create customer')

    def validate_email(self, email):

        email = Customer.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('Email already registered.')


class ItemRegistration(FlaskForm):
    name = StringField('Item', validators=[
                       DataRequired(), Length(min=2, max=20)])
    inStock = StringField('Amount', validators=[
        DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('Add item(s) to inventory')

    def validate_email(self, email):

        name = Customer.query.filter_by(name=name.data).first()

        if name:
            raise ValidationError('Item already registered in inventory.')


class SettingsForm(FlaskForm):
    companyName = StringField('Company name')
    companyCity = StringField('City')
    companyZip = StringField('Zip-code')
    companyAddress = StringField('Address')
    companyEmail = StringField('Email')
    companyPhone = IntegerField('Phone')
    companyMobile = IntegerField('Mobile')
    companyNumber = StringField('Company number')
    submit = SubmitField('Set site settings')
