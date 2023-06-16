from django.contrib.auth import get_user_model


def authenticate_with_email(email, password):
    User = get_user_model()
    user = User.objects.filter(email=email).first()
    print(user.is_active)

    if user:
        if user.check_password(password):
            return user
    return None
