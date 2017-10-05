Django Reauth
======


Django application for user authentication with ReAuth.
Application uses username given by ReAuth server as Django user. 

Usage
-----

Install djangoreauth

    python setup.py install

Add to settings.py

    AUTHENTICATION_BACKENDS = DEFAULT_SETTINGS.AUTHENTICATION_BACKENDS + (
        'djangoreauth.authenticationbackend.ReAuthBackend',
    )

Append 'djangoreauth' to installed apps

    INSTALLED_APPS = (
    ...,
    'djangoreauth',
    )

Add djangoreauth.urls to your app url patterns.

    patterns('',
    ...,
    url(r'^reauth/', include('djangoreauth.urls')),
    )

Add reauth_login_button tag to your login page

    {% load reauth_login_button %}
    ...

    {% reauth_login_button %}

Configure REAUTH settings to settings.py

    REAUTH_URL = "https://reauth.example.com"
    REAUTH_INSTANCE = "myinstance"
    REAUTH_APPLICATION = "myapp"

Configure application to ReAuth server.

Compile package
------------

To compile this package, run command

    python setup.py sdist --formats=gztar,zip

