def voto(valor):
    from datetime import date
    idade = date.today().year - valor
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nascimento = int(input('Digite seu ano de nascimento: '))
print({voto(nascimento)})
