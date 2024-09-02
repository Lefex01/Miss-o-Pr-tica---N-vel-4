from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

# Instância da classe Pessoa
pessoa1 = Pessoa("João", "123456", "2020-01-01", False)
pessoa1.imprimir_informacoes()

# Alterando os valores dos atributos usando setters
pessoa1.nome = "Ana"
pessoa1.numero_conta = "987654"
pessoa1.data_abertura_conta = "1995-12-12"
pessoa1.status = True

# Imprimindo as informações alteradas
pessoa1.imprimir_informacoes()

# Instância da classe PessoaFisica
pessoa_fisica = PessoaFisica("Carlos", "654321", "2019-05-15", "2000-01-01", "123.456.789-01", "98765432-1")
pessoa_fisica.imprimir_informacoes()

# Tentativa de atribuir um CPF inválido (menos de 14 caracteres)
try:
    pessoa_fisica.cpf = "12345678901"  # Menos de 14 caracteres
except ValueError as e:
    print(e)

# Atribuindo um CPF válido e imprimindo novamente as informações
pessoa_fisica.cpf = "123.456.789-01"
pessoa_fisica.imprimir_informacoes()

# Instância da classe PessoaJuridica
pessoa_juridica = PessoaJuridica("Empresa XYZ", "789456", "2018-03-20", "2015-12-12", "12.345.678/0001-00")
pessoa_juridica.imprimir_informacoes()

# Tentativa de atribuir um CNPJ inválido (menos de 18 caracteres)
try:
    pessoa_juridica.cnpj = "12345678/0001-00"  # Menos de 18 caracteres
except ValueError as e:
    print(e)

# Atribuindo um CNPJ válido e imprimindo novamente as informações
pessoa_juridica.cnpj = "12.345.678/0001-00"
pessoa_juridica.imprimir_informacoes()
