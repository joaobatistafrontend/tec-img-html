from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Agenda, Local
from .forms import AgendaForm

class AgendaCreateView(CreateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'form.html'  # Crie este arquivo HTML em seu diretório de modelos
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context ['local'] = Local.objects.all()
        return context 
    

def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            agenda = form.save()  # Salva o agendamento no banco de dados
            agenda.send_email() # Envia o e-mail com o comprovante em PDF
            form = AgendaForm()
    else:
        form = AgendaForm()

    return render(request, 'form.html', {'form': form})