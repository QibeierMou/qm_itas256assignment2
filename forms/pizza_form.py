from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, IntegerField, RadioField, SelectField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,NumberRange, EqualTo

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class CreateAccountForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Passwords must match")])
    role = RadioField("Role", choices=[("s", "Staff"), ("c", "Customer")], validators=[DataRequired()])
    submit = SubmitField("Create Account")

class PizzaForm(FlaskForm):
    type = SelectField("Type", validators=[DataRequired()])
    crust = SelectField("Crust", validators=[DataRequired()])
    size = SelectField("Size", validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired(), NumberRange(min=1, max=10)])
    price_per = FloatField("Price Per Pizza", validators=[DataRequired()])
    order_date = DateField("Order Date", validators=[DataRequired()])
    submit = SubmitField("Save Order")              