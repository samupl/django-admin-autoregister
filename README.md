django-admin-autoregister
=========================

Automatically register all your models in your django admn site.

Description
-----------

Using this django application, you don't have to manually register all your models in the admin site. 
All your models will be automatically registered, with a dynamically generated ModelAdmin class, that will format all your models nicely.

If you're just using the admin site to edit your models internally (if the only thing that you care about is a convenient way to edit your database), then this app should do it for you.

Usage
-----

All you have to do, is to copy the application into your app root, and append it into the *INSTALLED_APPS* settings variable:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # ...
    'django_autoregister',
)
```

After your project restarts (either by hand, or automatically, if you're using the developement server), you should see all your models and applications registered in your admin site.
