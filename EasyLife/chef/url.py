from django.urls import path
from . import views

urlpatterns = [
   path('_admin/login/',views.login_admin,name='login_admin'),
   path('_admin/contact/',views.welcome_contact,name='contact_admin'),
   path('_admin/welcome/',views.welcome_admin,name='welcome_admin'),
   path('_admin/client/',views.welcome_client,name='client'),
   path('delete_client/<int:id>',views.destroy_client),
   path('_admin/offre/',views.welcome_offre,name='offre'),
   path('delete_offre/<int:id>',views.destroy_offre),
   path('delete_contact/<int:id>',views.destroy_contact),
   path('logout_admin',views.logout_admin,name='logout_admin'),
   path('delete/<int:id>', views.destroy),  

]


