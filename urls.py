from django.conf.urls import *
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^admin/', include(admin.site.urls)),
    ### user facing views ###
    # static views
    (r'^$', TemplateView.as_view(template_name='start.html')),
    (r'^yes/$', TemplateView.as_view(template_name='end.html')),
    # form views
    (r'^topic/$','questions.views.topic_questions'),
    (r'^area/$','questions.views.area_questions'),
    (r'^supervisor/$','questions.views.supervisor_questions'),
    (r'^career/$','questions.views.career_questions'),
)
