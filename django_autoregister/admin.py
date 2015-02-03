from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_models, get_app
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.conf import settings


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



def auto_register(*app_list):
    for app_name in app_list:
        try:
            app_models = get_app(app_name)
        except ImproperlyConfigured:
            continue
        for model in get_models(app_models):
            try:
                admin.site.register(model, AutoDisplayAdmin)
            except AlreadyRegistered:
                pass


app_list = [app for app in settings.INSTALLED_APPS]
auto_register(*app_list)
