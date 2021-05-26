from django.apps import AppConfig
from django.db.models.signals import pre_save
from django.dispatch import receiver


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # importing model classes
        from .models import MyUser  # or...
        MyUser = self.get_model('MyUser')
        from .models import User
        # registering signals with the model's string label
        pre_save.connect(receiver, sender='users.MyUser')
        pre_save.connect(receiver, sender='auth.User')
