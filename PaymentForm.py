from wtforms import RadioField, EmailField, StringField, SelectField, TextAreaField, Form, BooleanField, validators

# add phone number, email, full name fields

class CreatePaymentForm(Form):
    card_holder_name = StringField('Card Holder Name', [validators.length(min=1, max=150), validators.DataRequired()])
