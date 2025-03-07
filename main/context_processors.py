from django.contrib.auth.models import User

def get_user(request):
    if request.user.is_authenticated:
        context = {
            'user': request.user
        }
        return context
    return {'user': None}
