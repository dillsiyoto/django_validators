from django.core.exceptions import ValidationError
import re 
import socket


def validate_email_self(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValidationError("Неправильный формат")

def validate_username(username):
    if len(username) < 3:
        raise ValidationError("Никнейм должен содержать больше 3 символов")
    if len(username) > 30:
        raise ValidationError("Никнейм должен содержать меньше 30 символов")
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValidationError("Никнейм должен содержать буквы верхнего и нижнего регистра, цифры и нижнее подчеркивание")
    
def validate_password(password):
    if not re.search(r'[a-zA-Z]', password):
        raise ValidationError("Пароль должен содержать буквы верхнего и нижнего регистра")
    if not re.search(r'[0-9]', password):
        raise ValidationError("Пароль должен содержать цифру")
    if not re.search(r'[!@#&?]', password):
        raise ValidationError("Пароль должен содержать спецсимвол")
    if len(password) < 8:
        raise ValidationError("Пароль должен быть больше 8 символов")
    
def domain_check(value):
    try:
        validate_email_self(value)
        socket.gethostbyname(value.split('@')[-1])
    except(ValidationError, socket.gaierror):
        raise ValidationError('Неправильная почта или домен не существует')