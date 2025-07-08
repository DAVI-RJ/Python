#exercicio 1 
print('Bem-vindo, meu nome e Davi Ribeiro.')

valor = float(input('Valor do produto: R$ '))
#calculo do juros 
def valor_juros(parcelas):
    if parcelas <= 3:
        return valor
    elif parcelas == 4 or parcelas == 5:
        return valor * 1.04
    elif parcelas == 6 or parcelas <= 8:
        return valor * 1.08
    elif parcelas == 9 or parcelas <= 12:
        return valor * 1.16
    elif parcelas >= 13:
        return valor * 1.32
    else: 
        return None 
   
parcelas = int(input('quantidade de parcelas: '))
#valor total chama a função valor com juros
valor_total = valor_juros(parcelas)
n_parcelas = parcelas
#calculo para valor mensal da tabela
if valor_total is not None:
    valor_mensal = valor_total / n_parcelas
    print(f'Valor mensal: R${valor_mensal:.2f}')
    print(f'valor total do produto com juros: R$ {valor_total:.2f}')