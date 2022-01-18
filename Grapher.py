# INICIO PRODUÇÃO
# pedidos finalizados por dia
# meta minima
# meta maxima
# lucro diario
# estimativa de lucro mensal
# FIM PRODUÇÃO
# =============================================
# INICIO GESTÃO
# envio de arquivo com dados 
# gerar relatório para impressão
# opção para arquivar relatório ou apagar
# FIM GESTÃO

from datetime import date, datetime
import sys
import time
from fpdf import FPDF
import sched

horario = time.ctime()
scheduler = sched.scheduler()
a = horario
frmt = a[11:16]
print("Horário atual: {}".format(frmt))
hs = str(input('Digite o horário de término do seu turno (H:M) ==> '))
print('O seu turno encerra {}, neste horário o programa irá encerrar.'.format(hs))

def Inicio():
    while True:  
        valor = str(input('Digite o valor da O.D ===> '))
        OD = int(input("Digite o número da O.D ===> "))
        OP = str(input("Digite o primeiro nome do Operador ==> "))
        datet = datetime.now()
        txt = datet.strftime('%d/%m/%Y | %Hh %Mm %Ss')
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Times', '', 14)
        pdf.multi_cell(200,12, "|| Valor: {} | OD: {} | OP: {} | GERADO EM: {} ||".format(valor, OD, OP, txt),0, 'C', False)
        pdf.output('vadias.pdf', 'F')
        continue
def Pausa():
    if hs == frmt:
        print('Os processos serão finalizados')
        time.sleep(3)
        sys,exit()
scheduler.enter(delay=2, priority=0, action=Pausa)
try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('CABO')
Inicio()