# Exercício 2: 

#lista de valores
valores = {
    0: 16.00,
    1: 18.00,
    2: 22.00,
}
#lista de tamanhos
tamanhos = {
	0: "p",
	1: "m",
	2: "g",
}
#lista tipos
tipos = {
	"BA",
	"FF",
}
# variavel para armazenar o valor de file de frango
FF = valores[0] - 1, valores[1] - 1, valores[2] - 1

menu = [
	#tamanho, tipo, valor
	(f"CARDAPIO | tamanho (p - pequeno, m - medio, g - grande)"
  " Bife Acebolado(BA), File de Frango(FF)"
	),  
	({tamanhos[0]}, {valores[0]}, {FF[0]}),  
	({tamanhos[1]}, {valores[1]}, {FF[1]}),
	({tamanhos[2]}, {valores[2]}, {FF[2]}),
]

print("Bem-vindo, meu nome e Davi Ribeiro")

print(menu)

# variável global para acumular o valor total
total = 0  

#função para gerar o pedido do cliente
def cliente():
	global total

	tamanho_map = {"p": 0, "m": 1, "g": 2}

	while True:
			sabor = input("Entre com o sabor desejado (BA / FF): ")
			if sabor not in tipos:
				print("Opção de sabor inválida, tente novamente.")
				continue  
			
			tamanho_escolhido = input("Qual o tamanho da marmita (p/m/g)? ")
			if tamanho_escolhido not in tamanho_map:
				print("Opção de tamanho inválida, tente novamente.")
				continue  

			# apos ter escolhido sabor e tamanho
			if sabor == "BA":
					valor = valores[tamanho_map[tamanho_escolhido]]
			else:
					valor = FF[tamanho_map[tamanho_escolhido]]

			total += valor

			print(f"Seu pedido foi {sabor} tamanho, {tamanho_escolhido}, valor: R$ {valor:.2f}")

			adicionar = input("Deseja pedir mais alguma coisa? (S/N) ")

			if adicionar == "S":
					# volta para o início para novo pedido
					continue  
			
			else:
					print(f"Valor total do pedido: R$ {total:.2f}")
					# encerra a função
					break  
			
cliente()