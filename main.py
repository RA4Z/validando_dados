from Cpf_Cnpj import Documento
from TelefonesBr import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

cep = '89275000'
objeto_cep = BuscaEndereco(cep)
print(objeto_cep.acessa_via_cep())


"""cadastro = DatasBr()
print(cadastro.tempo_cadastro())"""

"""telefone = '554799585728'
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)"""

"""exemplo_cnpj = '35379838000112'
exemplo_cpf = '12656738962'
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)"""