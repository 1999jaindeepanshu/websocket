from django.apps import AppConfig


class ChannelsTutConfig(AppConfig):
    name = 'channels_tut'

    def ready(self):
        import channels_tut.signals


