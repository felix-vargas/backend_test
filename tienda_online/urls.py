from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('usuarios', views.get_users, name='get users'),
    path('register', views.create_user, name='create new user'),
    path('login',views.login, name='login'),
    path('producto', views.create_product, name='create product'),
    path('productos', views.list_products, name='create product'),
    
    path('categoria', views.create_category, name='create category'),
    path('categorias', views.get_categories, name='get categories'),
    #listos los roles
    path('rol', views.create_rol, name='create rol'),
    path('roles', views.get_roles, name='get roles'),
    path('compra', views.send_email, name='compra'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)