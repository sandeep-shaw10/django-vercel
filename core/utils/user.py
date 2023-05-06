from django.contrib.auth import get_user_model

def allUsers():
    error, users = False, None
    try:
        User = get_user_model()
        users = User.objects.all()
    except Exception as e:
        error = e
    return { 'users': users, 'error': error }
