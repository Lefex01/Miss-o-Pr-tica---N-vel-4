from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, numero_conta, data_abertura_conta, data_abertura_empresa, cnpj):
        super().__init__(nome, numero_conta, data_abertura_conta, True)
        self.__data_abertura_empresa = data_abertura_empresa
        self.__cnpj = cnpj

    @property
    def data_abertura_empresa(self):
        return self.__data_abertura_empresa

    @data_abertura_empresa.setter
    def data_abertura_empresa(self, data_abertura_empresa):
        self.__data_abertura_empresa = data_abertura_empresa

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        if len(cnpj) != 18:
            raise ValueError("O CNPJ deve conter 18 caracteres (no formato 00.000.000/0001-00).")
        self.__cnpj = cnpj

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f"Data de Abertura da Empresa: {self.__data_abertura_empresa}")
        print(f"CNPJ: {self.__cnpj}")
