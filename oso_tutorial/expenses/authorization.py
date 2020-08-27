from .models import User

class Guest(Actor):
    """Anonymous user."""
    def __str__(self):
        return "Guest"

def get_user(get_response):

    def middleware(request):
        email = request.headers.get('user')
        if email:
            request.current_user = User.objects.filter(email=email).first()
        else:
            request.current_user = Guest()

        return get_response(request)

    return middleware
