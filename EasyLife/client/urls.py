from django.urls import path
from . import views
urlpatterns = [
    path('client/login/',views.homeLogin,name="login_Client"),
    path('client/register/',views.registerPage,name="register_client"),
    path('client/profile/',views.getDetailClient,name="profile_client"),
    path('client/update/',views.modifierClient,name="modifier_client"),
    path('client/listOffre',views.GetAllOffre,name="list_offre"),
    path('client/<int:idC>/DetailsOffre',views.GetDetailsOffre,name="Details_offre"),
    path('client/myoffre',views.GetOffreClient,name="offre_by_client"),
    path('client/update/<int:idO>/offre',views.ModifierOffre,name="modifier_Offre"),
    path('logout',views.LogOut,name='logout'),
    path('client/delete',views.DeleteClient,name="delete_client"),
    path('client/myoffre/<int:idO>/delete',views.DeleteOffre,name="delete_Offre"),
    path('client/offre/listPost/<int:idO>',views.GetListPostuler,name="list_postuler"),

]