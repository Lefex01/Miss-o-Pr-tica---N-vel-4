from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, numero_conta, data_abertura_conta, data_nascimento, cpf, rg):
        super().__init__(nome, numero_conta, data_abertura_conta, True)
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 14:
            raise ValueError("O CPF deve conter 14 caracteres (no formato 000.000.000-00).")
        self.__cpf = cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f"Data de Nascimento: {self.__data_nascimento}")
        print(f"CPF: {self.__cpf}")
        print(f"RG: {self.__rg}")
