from wtforms import ValidationError

def has_digit(password):
    return any(c.isdigit() >= 1 for c in password)


def has_upper_and_lower_case(password):
    letters = set(password)
    is_mixed_case = (
        any(letter.islower() for letter in letters) and
        any(letter.isupper() for letter in letters))
    return is_mixed_case


def has_digit_and_upper_lower_exist(password):
    return has_digit(password) and has_upper_and_lower_case(password)


def is_password_short(password):
    min_password_length = 10
    passwd_length = len(password)
    if passwd_length < min_password_length:
        return True
    

def is_password_valid(self, field):
    bad_password_message = """Пароль должен:\n
                              быть больше 10 символов,\n
                              содержать буквы и цифры,\n
                              содержать буквы разного регистра.\n"""
    if (is_password_short(field.data) or 
        not has_digit_and_upper_lower_exist(field.data)):
        raise ValidationError(bad_password_message)