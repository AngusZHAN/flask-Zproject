from wtforms import (
    Form, 
    StringField, 
    TextAreaField, 
    PasswordField, 
    BooleanField, 
    SubmitField, 
    validators, 
    ValidationError,
    )
from ..models import User


class LoginForm(Form):
    username = StringField('用户名', validators=[validators.DataRequired(), validators.Length(1, 64)])
    password = StringField('密码', validators=[validators.DataRequired()])
    remember_me = BooleanField('保持连续登录')


class RegisterForm(Form):
    username = StringField('用户名', validators=[validators.Length(min=1, max=20)])
    telephone = StringField('手机号码', validators=[validators.Length(min=5, max=15)])
    password = PasswordField('密码', validators=[validators.DataRequired(),
                                               validators.EqualTo('confirm', message='密码必须一致')])
    confirm = PasswordField('确认密码')
    accept_tos = BooleanField('我自愿接受服务条款', [validators.DataRequired()])

    def validate_telephone(self, field):
        if User.query.filter_by(telephone=field.data).first():
            raise ValidationError('手机已被注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被注册')
