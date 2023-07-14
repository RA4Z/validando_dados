from Cpf_Cnpj import Documento
import re

padrao = '\w{5,50}@[a-z]{3,10}.com(.br)?'
texto = 'rraz639@gmail.com.br'
respostas = re.search(padrao, texto)
print(respostas.group())


"""exemplo_cnpj = '35379838000112'
exemplo_cpf = '12656738962'

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)"""