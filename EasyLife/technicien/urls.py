from django.urls import path
from . import views
urlpatterns = [
   path('technicien/register-29/',views.register,name='register'),
    path('technicien/login-29/',views.login,name='login'),
    path('technicien/welcome/',views.welcome,name='welcome'),
    path('technicien/postulation/',views.postulation_page,name='postuler'),
    path('technicien/profile/',views.profile,name='profile'),
    path('technicien/update/',views.update,name='update'),
    path('technicien/details/<int:id>',views.Detailsoffre,name='Details'),
    
    path('delete_postule/<int:id>', views.destroy_postuler),  
    path('logout',views.logout,name='logout_tech'),
    path('error/',views.error,name='404'),
    path('delete',views.destroy,name='destroy'),
]