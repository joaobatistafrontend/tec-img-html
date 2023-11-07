from django.db import models
import random

from django.core.mail import EmailMessage
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from reportlab.platypus import Image

class Local(models.Model):
     cidade = models.CharField(max_length=255)
     endereco = models.CharField(max_length=255)
     numeracao = models.CharField(max_length=255)
     logradouro = models.CharField(max_length=255,  null=True, blank=True)
     mapa_link = models.URLField(default=' ', max_length=1000)
     def __str__(self):
          logradouro = self.logradouro if self.logradouro else ''  # Use o logradouro se não for nulo, caso contrário, uma string vazia
          return f"{self.cidade} - {self.endereco} - {self.numeracao} - {logradouro}"

class Opcoes(models.Model):
     opcoes = models.CharField(max_length=255)
     valor = models.DecimalField(max_digits=10, decimal_places=2)

     def __str__(self):
          return f"{self.opcoes} - {self.valor}"
     
def gerar_protocolo():
     while True:
          protocolo = random.randint(1, 10000000000)
          if not Agenda.objects.filter(protocolo=protocolo).exists():
               return protocolo

class Agenda(models.Model):
     nome = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     local = models.ForeignKey(Local, on_delete=models.CASCADE)
     opcao = models.ForeignKey(Opcoes, on_delete=models.CASCADE)
     data = models.DateField(verbose_name='Data de Agendamento')
     protocolo = models.CharField(max_length=100, default=gerar_protocolo)


     def send_email(self):
          nome = self.nome
          email = self.email
          opcoes = self.opcao
          local = f"{self.local}"
          data = self.data
          protocolo = self.protocolo
          assunto = 'Comprovante de Agendamento'




          # Criação de um arquivo PDF com os dados do formulário
          buffer = BytesIO()
          doc = SimpleDocTemplate(buffer, pagesize=letter)
          styles = getSampleStyleSheet()
          elements = []

          image = Image("templates/logo.png", width=200, height=200)
          elements.append(image)


          elements.append(Paragraph('Comprovante de Agendamento', styles['Title']))
          elements.append(Spacer(1, 12))

          data_table = [
               ['Nome:', nome],
               ['Email:', email],
               ['Opções de Agendamento:', opcoes],
               ['Local:', Paragraph(local, styles['Normal'])],  # Utilize o estilo 'Normal' para quebrar a linha
               ['Data de Agendamento:', data],
               ['Gerar Prrotocolo', protocolo]
          ]

          table = Table(data_table, colWidths=300, rowHeights=30)
          table.setStyle(TableStyle([
               ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
               ('GRID', (0, 0), (-1, -1), 1, colors.black),
          ]))

          elements.append(table)
          doc.build(elements)

          # Anexa o PDF ao email
          buffer.seek(0)
          email = EmailMessage(
               subject=assunto,
               from_email='jbbuno007@gmail.com',
               to=[email],
          )
          email.attach('comprovante.pdf', buffer.read(), 'application/pdf')
          email.send()