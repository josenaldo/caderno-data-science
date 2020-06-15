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
    return data[0:2]

def extrai_mes(data):
    return data[3:5]

def extrai_ano(data):
    return data[6:10]


def validar_dia(data):
    dia_str = extrai_dia(data)

    try:
        dia = int(dia_str)
        if(dia < 0 or dia > 31):
            raise ValidationError(
                f"Valor informado para dia deve estar entre 1 e 31."
                f" Valor incorreto: '{dia_str}'"
            )

    except ValueError as error:
        raise ValidationError(
            f"Valor informado para dia não é um número válido."
            f" Valor incorreto: '{dia_str}'"
        )



def validar_mes(data):

    mes_str = extrai_mes(data)

    try:
        mes = int(mes_str)

        if(mes < 0 or mes > 12):
            raise ValidationError(
                f"Valor informado para mês deve estar entre 1 e 12."
                f" Valor incorreto: '{mes_str}'"
            )

    except ValueError as error:
        raise ValidationError(
            f"Valor informado para mês não é um número válido."
            f" Valor incorreto: '{mes_str}'"
        )


def validar_ano(data):
    ano_str = extrai_ano(data)

    try:
        ano = int(ano_str)
    except ValueError as error:
        raise ValidationError(
            f"Valor informado para ano não é um número válido."
            f" Valor incorreto: '{ano_str}'"
        )


def validar_formato_data(data):
    formato = re.search("[0-3]\d/[0-1]\d/\d\d\d\d", data)
    if(not formato):
        raise ValidationError(
            f"Valor informado para data não corresponde ao formato DD/MM/AAAA."
            f" Valor incorreto: '{data}'"
        )


def validar_dia_mes(data):
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
            f"O mês informado para a data possui no máximo {dias_meses[mes]} dias."
            f" Valor incorreto: '{dia}'"
        )


def eh_ano_bissexto(data):

    ano = int(extrai_ano(data))

    return  ((ano % 4 == 0) and ((ano % 400 == 0) or (ano % 100 != 0)) )


def data_por_extenso(data):

    try:
        validar_formato_data(data)
        validar_ano(data)
        validar_mes(data)
        validar_dia(data)
        validar_dia_mes(data)

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
        "22/12/1984", "01/01/290", "9091293781", "32/01/1998",
        "30/02/2000", "26/45/3009"
        ]

    for data in datas:
        print(f" {data} ".center(60, "*"))
        print(data_por_extenso(data))
