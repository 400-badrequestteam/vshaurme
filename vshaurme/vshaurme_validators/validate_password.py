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
    return passwd_length < min_password_length


def is_password_valid(self, field):
    bad_password_message = """Пароль должен:\n
                              быть больше 10 символов,\n
                              содержать буквы и цифры,\n
                              содержать буквы разного регистра.\n"""
    first_condition = is_password_short(field.data)
    second_condition = has_digit_and_upper_lower_exist(field.data)
    if first_condition or not second_condition:
        raise ValidationError(bad_password_message)
