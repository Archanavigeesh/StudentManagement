from django.urls import path
from . import views

urlpatterns = [
    path('',views.fnlogin,name='login'),
    path('StudentRegistration',views.fnstudentregistration,name='StudentRegistration'),
    path('adminhome',views.fnadminhome,name='adminhome'),
    path('inactive',views.fninactivestd,name='inactive'),
    path('active',views.fnactivestd,name='active'),
    path('stdhome',views.fnstdhome,name='stdhome'),
    path('updateprofile',views.fnstdupdate,name='updateprofile'),
    path('changestate',views.fnchangestate,name='changestate'),
    path('logout',views.fnlogout,name='logout'),
    path('adminstdreg',views.fnadminstdreg,name='adminstdreg'),
]
