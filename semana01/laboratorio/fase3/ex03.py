# 3.3 Crie um algoritmo em Python que leia e valide as seguintes informações:
#   Nome: maior que 3 caracteres;
#   Idade: entre 0 e 150;
#   Salário: maior que zero;
#   Sexo: 'f' ou 'm';
#   Estado Civil: 's', 'c', 'v', 'd';

SEXOS = {
    'f': 'FEMININO',
    'm': 'MASCULINO',
    'o': 'OUTROS E NÃO BINÁRIOS',
}

ESTADOS_CIVIS = {
    's': 'SOLTEIRO/SOLTEIRA',
    'c': 'CASADO/CASADA',
    'v': 'VIÚVO/VIÚVA',
    'd': 'SEPARADO/SEPARADA',
}

def ler_nome():
    """ Lê o nome do usuário

    Função que lê o nome do usuário. O nome deve ter mais de 3
    caracteres.
    """

    nome = None
    while (True):
        try:
            nome = input("Insira o nome: ")
            if(len(nome) <= 3):
                raise ValueError(
                    "Nome inválido. "
                    "É preciso informar ao menos 4 caracteres. "
                    f"Valor incorreto: {nome}"
                )
            else:
                break
        except ValueError as error:
            print("Ocorreu um erro durante a execução do sistema.")
            print(f"\tMensagem: {error}")

    return nome


def ler_idade():
    """ Lê a idade do usuário

    Função que lê o idade do usuário. O idade deve ter um valor entre
    0 e 150 anos.
    """

    idade = None
    while (True):
        try:
            idade = int(input("Insira a idade: "))
            if(idade < 0 or idade > 150):
                raise ValueError(
                    "Idade inválida. "
                    "É preciso informar um valor entre 0 e 150. "
                    f"Valor incorreto: {idade}"
                )
            else:
                break
        except ValueError as error:
            print("Ocorreu um erro durante a execução do sistema.")
            print(f"\tMensagem: {error}")

    return idade


def ler_salario():
    """ Lê a salario do usuário

    Função que lê o salario do usuário. O salario deve ter um valor
    maior que zero.
    """

    salario = None
    while (True):
        try:
            salario = float(input("Insira o salário: "))
            if(salario < 0):
                raise ValueError(
                    "Salario inválido. "
                    "É preciso informar um valor maior que 0. "
                    f"Valor incorreto: {salario}"
                )
            else:
                break
        except ValueError as error:
            print("Ocorreu um erro durante a execução do sistema.")
            print(f"\tMensagem: {error}")

    return salario


def ler_sexo():
    """ Lê a sexo do usuário

    Função que lê o sexo do usuário. O sexo deve ter um dos seguintes
    valores:
        f - feminino
        m - masculino
        o - outros e não binários
    """

    sexo = None
    while (True):
        try:
            sexo = input("Insira o sexo (f | m): ")
            if(sexo not in SEXOS ):
                raise ValueError(
                    "Sexo inválido. "
                    "É preciso informar m ou f. "
                    f"Valor incorreto: {sexo}"
                )
            else:
                break
        except ValueError as error:
            print("Ocorreu um erro durante a execução do sistema.")
            print(f"\tMensagem: {error}")

    return sexo

def ler_estado_civil():
    """ Lê o estado civil do usuário

    Função que lê o estado civil do usuário. O estado civil deve conter
    um dos seguiontes valores:
        s: Solteiro/Solteira
        c: Casado/Casada
        v: Viúvo/Viúva
        d: Separado/Separada
    """

    estado_civil = None
    while (True):
        try:
            estado_civil = input("Insira o estado_civil (s | c | v | d): ")
            if(estado_civil not in ESTADOS_CIVIS):
                raise ValueError(
                    "Estado civil inválido. "
                    "É preciso informar 's', ou 'c', ou 'v', ou 'd. "
                    f"Valor incorreto: {estado_civil}"
                )
            else:
                break
        except ValueError as error:
            print("Ocorreu um erro durante a execução do sistema.")
            print(f"\tMensagem: {error}")

    return estado_civil

# Leitura das variáveis
nome = ler_nome()
idade = ler_idade()
salario = ler_salario()
sexo = ler_sexo()
estado_civil = ler_estado_civil()
# ler estado civil

# Exibição do relatório
print(f"""
Nome: {nome}
Idade: {idade}
Salário: R$ {salario:.2f}
Sexo: {SEXOS[sexo]}
Estado Civil: {ESTADOS_CIVIS[estado_civil]}
-------------------------------------------------
""")