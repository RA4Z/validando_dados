from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if tipo_documento == 'cpf':
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF Inválido!!')
            
        elif self.tipo_documento == 'cnpj':
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ Inválido!!')
            
        else:
            raise ValueError('Tipo de Documento Inválido!!')

    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        elif self.tipo_documento == 'cnpj':
            return self.format_cnpj()

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida!!')
        
    def cnpj_eh_valido(sel,documento):
        if len(documento) == 14:
            validador = CNPJ()
            return validador.validate(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida!!')
    
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
            