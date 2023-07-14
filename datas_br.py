from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril',
            'Maio', 'Junho', 'Julho', 'Agosto',
            'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dia_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        numero_dia_semana = self.momento_cadastro.weekday()
        return dia_semana[numero_dia_semana]