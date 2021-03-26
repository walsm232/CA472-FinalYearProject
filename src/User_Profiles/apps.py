from django.apps import AppConfig

class UserProfilesConfig(AppConfig):
    name = 'User_Profiles'

    def ready(self):
       import User_Profiles.signals