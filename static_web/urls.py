from django.conf.urls import url, patterns
from static_web.views import *

urlpatterns = patterns(
    '',
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^about/$',
        AboutView.as_view(),
        name='about'),
    url(r'^clases/$',
        ClasesView.as_view(),
        name='clases'),
    url(r'^contact/$',
        ContactView.as_view(),
        name='contact'),
    url(r'^schedule/$',
        ScheduleView.as_view(),
        name='schedule'),
    url(r'^trainer/$',
        TrainerView.as_view(),
        name='trainer'),
)
