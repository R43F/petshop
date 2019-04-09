from django.urls import path
from petshop.core.views import home, estoque, agendamento
app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('estoque/', estoque, name='estoque'),
    path('agendamento/', agendamento, name='agendamento'),
]
