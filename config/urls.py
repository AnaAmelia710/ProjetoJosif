from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from app.views import (pagina_inicial,lista_pessoas,lista_pontos_coleta,lista_tipos_residuos,lista_campanhas,lista_participacoes,lista_historico, cadastro,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_inicial, name='pagina_inicial'),
    path('pessoas/', lista_pessoas, name='lista_pessoas'),
    path('pontos_coleta/', lista_pontos_coleta, name='lista_pontos_coleta'),
    path('tipos_residuos/', lista_tipos_residuos, name='lista_tipos_residuos'),
    path('campanhas/', lista_campanhas, name='lista_campanhas'),
    path('participacoes/', lista_participacoes, name='lista_participacoes'),
    path('historico/', lista_historico, name='lista_historico'),
]
urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
]