import re
from django.core.exceptions import ValidationError

def validate_instagram_password(password, username=None):
    # 1. Minimum length
    if len(password) < 6:
        raise ValidationError("Password must be at least 6 characters long.")

    # 2. At least 1 letter required
    if not re.search(r"[A-Za-z]", password):
        raise ValidationError("Password must contain at least one letter.")

    # 3. Very common passwords block
    common = ["123456", "password", "qwerty", "abcdef", "111111"]
    if password.lower() in common:
        raise ValidationError("This password is too easy. Choose a stronger one.")

    # 4. Don’t match username
    if username and username.lower() in password.lower():
        raise ValidationError("Password should not contain your username.")

    # 5. No full name or easy words (optional)
    easy_words = ["instagram", "insta", "login", "admin", "user"]
    if any(word in password.lower() for word in easy_words):
        raise ValidationError("Password is too simple. Try another one.")

    return True
