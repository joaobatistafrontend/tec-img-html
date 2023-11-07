from django.urls import path
from .views import AgendaCreateView, criar_agendamento

urlpatterns = [
    # Outras URLs do seu aplicativo
    #path('', AgendaCreateView.as_view(), name='home'),
    path('', criar_agendamento, name='home'),

]