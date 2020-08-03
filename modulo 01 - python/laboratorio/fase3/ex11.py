# 3.11 Construa uma função que receba uma data no formato DD/MM/AAAA e devolva
# uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a
# data e retorne NULL caso a data seja inválida.

import re

MESES = {
    '01': 'Janeiro',
    '02': 'Fevereiro',
    '03': 'Março',
    '04': 'Abril',
    '05': 'Maio',
    '06': 'Junho',
    '07': 'Julho',
    '08': 'Agosto',
    '09': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro',
}

class ValidationError(Exception):
    pass


def extrai_dia(data):
    """Extrai o dia, com 2 dígitos, da data"""
    return data[0:2]


def extrai_mes(data):
    """Extrai o mês, com 2 dígitos, da data"""
    return data[3:5]


def extrai_ano(data):
    """Extrai o ano, com 4 dígitos, da data"""
    return data[6:10]


def validar_formato_data(data):
    """Valida se o formato da data é dd/mm/aaaa"""

    formato = re.search("[0-3]\d/[0-1]\d/\d\d\d\d", data)
    if(not formato):
        raise ValidationError(
            f"Valor informado para data não corresponde ao formato DD/MM/AAAA."
            f" Valor incorreto: '{data}'"
        )


def validar_ano(data):
    """Valida se o ano tem 4 digitos e se é um número"""

    ano_str = extrai_ano(data)

    has_four_digits = len(ano_str) == 4
    is_number = ano_str.isdigit()

    if( not (has_four_digits and is_number)):
        raise ValidationError(
            f"Valor informado para ano não é um número válido."
            f" Valor incorreto: '{ano_str}'"
        )

def validar_mes(data):
    """Valida se o mês informado está dentro da lista de meses"""
    mes_str = extrai_mes(data)

    try:
        mes = MESES[mes_str]
    except KeyError as error:
        raise ValidationError(
                f"Valor informado para mês deve estar entre 1 e 12."
                f" Valor incorreto: '{mes_str}'"
            )

def validar_dia(data):
    """Valida se o dia

    Valida se o dia é maior ou igual a 1 e menor ou igual ao máximo de dias
    do mes.

    No caso de ser o dia 29 de fevereiro, leva em conta se o ano é bissexto.
    """
    dias_meses = {
        '01': 31,
        '02': 28,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31,
    }

    dia = extrai_dia(data)
    mes = extrai_mes(data)

    if(eh_ano_bissexto(data)):
        dias_meses['02'] = 29

    if(int(dia) > dias_meses[mes]):
        raise ValidationError(
            f"Dia inválido. O valor do dia deve ser entre 01 e {dias_meses[mes]} dias."
            f" Valor incorreto: '{dia}'"
        )


def eh_ano_bissexto(data):
    """Verifica se o ano é bissexto"""

    ano = int(extrai_ano(data))

    return  ((ano % 4 == 0) and ((ano % 400 == 0) or (ano % 100 != 0)))


def data_por_extenso(data):
    """Converte uma data no formado DD/MM/AAAA em uma data por extenso.

    Se a data for inválida, retorna None.
    """
    try:
        validar_formato_data(data)
        validar_ano(data)
        validar_mes(data)
        validar_dia(data)

        dia = int(extrai_dia(data))
        mes = extrai_mes(data)
        ano = extrai_ano(data)

        mes_por_extenso = MESES[mes]

        data_por_extenso = f"{dia} de {mes_por_extenso} de {ano}"

        return data_por_extenso
    except ValidationError as error:
        print("Ocorreu um erro ao validar a data:")
        print("\t", error)
        return None

if __name__ == "__main__":
    datas = [
        "16/06/2020", # DATA VÁLIDA
        "00/01", # FALTA O ANO
        "manga", # DATA INVÁLIDA FORA DO FORMATO
        "04/15/1981", # DATA INVÁLIDA PORQUE O MÊS NÃO EXISTE
        "12/06/190", # DATA INVÁLIDA PORQUE O ANO TEM 3 CARACTERES
        "30/02/2012", # DATA INVÁLIDA PORQUE O MÊS 02 NÃO TEM DIA 30
        "30/11", # FALTA O ANO
        "25/08/maga", #ANO INVALIDO
        "12/-4/1980", #MES negativo
        "31/04/1587", #
        "-2/01/1995", # DATA INVÁLIDA PORQUE DIA NEGATIVO
        "32/10/2005", # DATA INVÁLIDA PORQUE DIA É MAIOR QUE 31
        "30/02/2006", # MÊS 02 SÓ TEM 28 OU 29 DIAS
        "31/04/2006", # MÊS 4 TEM 30 DIAS
        "31/06/2007", # MêS 06 TEM 30 DIAS
        "29/02/2001", # NÃO É ANO BISSEXTO
        "29/02/1900", # NÃO É ANO BISSEXTO
        "29/02/2000", # É ANO BISSEXTO
        "29/02/2004", # É ANO BISSEXTO
        ]

    for data in datas:
        print(f" {data} ".center(60, "*"))
        print(data_por_extenso(data))
