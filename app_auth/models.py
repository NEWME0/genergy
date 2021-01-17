from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
        Base user model.
    """

    @classmethod
    def get_my_message(cls):
        return 'your message'
