from django.urls import path

from .views import index, project_mono, project_pystagram, project_jjinmall


app_name = 'portfolio'

urlpatterns = [
    path('',index, name='index'),
    path('project/monoground/', project_mono, name='mono'),
    path('project_pystagram/', project_pystagram, name='pystagram'),
    path('project_jjinmall/', project_jjinmall, name='jjinmall'),
]