from django.apps import AppConfig
from django.contrib import admin
from django.db import models


class AutoDisplayAdmin(admin.ModelAdmin):
    list_links_fields = ('CharField',
                         'IntegerField',
                         'AutoField',
                         'DateField',
                         'DateTimeField',
                         'SlugField',
                         'BigIntegerField',
                         'EmailField',
                         'BooleanField',
                         'DecimalField',
                         'FloatField',
                         'IPAddressField',
                         'GenericIPAddressField',
                         'NullBooleanField',
                         'PositiveIntegerField',
                         'PositiveSmallIntegerField',
                         'UrlField',
                         'TimeField',)
    list_display_fields = list_links_fields + ('ForeignKey', )

    def __init__(self, *args, **kwargs):
        admin.ModelAdmin.__init__(self, *args, **kwargs)
        self.list_display = []
        self.list_display_links = []
        for field in args[0]._meta.fields:
            if field.get_internal_type() in self.list_display_fields:
                self.list_display.append(field.name)
            if len(self.list_display_links) < 2 and field.get_internal_type() in self.list_links_fields:
                self.list_display_links.append(field.name)


class DjangoAutoRegisterConfig(AppConfig):

    name = 'django_autoregister'
    verbose_name = 'Django model auto registration plugin'

    def ready(self):
        all_models = models.get_models()
        registered_models = admin.site._registry

        for model in all_models:
            if model in registered_models:
                continue
            admin.site.register(model, AutoDisplayAdmin)