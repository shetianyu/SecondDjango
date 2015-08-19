__author__ = 'shety'

from django.conf.urls import *



from Blog.views import *

urlpatterns = patterns('Blog.views',
    url(r'^$', archive),
    url(r'^h2/', archiveh2),
    url(r'^h3/', wyethdone),
    url(r'^wyeth/', wyethlist),
    url(r'^LorealDone/',lorealdone ),
    url(r'^Loreal/', loreallist),
)