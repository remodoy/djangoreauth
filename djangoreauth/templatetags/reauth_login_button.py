from django import template
from django.conf import settings
from django.utils.translation import ugettext as _


register = template.Library()


@register.simple_tag(name="reauth_login_button")
def reauth_login_button():
    conf = {
        'reauth_url': settings.REAUTH_URL,
        'reauth_instance': settings.REAUTH_INSTANCE,
        'reauth_application': settings.REAUTH_APPLICATION,
        'login': _("Login")
    }
    return """
    <div class="btn-group">
        <button id="redirect" class="btn btn-info">%(login)s</button>
    </div>

<script>
    var options = {
        authEndpoint: '%(reauth_url)s',
        instance: '%(reauth_instance)s',
        application: '%(reauth_application)s',
        applicationOrigin: window.location.origin,
        useRedirect: true
    };

    const redirectButton = document.getElementById('redirect');
    redirectButton.onclick = function () {
        ReAuth.configure(options);
        ReAuth.startAuthentication();
    };
</script>
    """ % conf
