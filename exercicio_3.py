#exercicio 3

#modelos de camiseta 
modelos = ["MCS", "MLS", "MCE", "MLE"]

#valor de cada modelo
valor_modelo = {
    "MCS": 1.80,
    "MLS": 2.10,
    "MCE": 2.90,
    "MLE": 3.20
}

tipo_entrega = {

		0: 100.00,
		1: 100.00,
		2: 200.00
	}

#variaveis globais acumuladoras 
pedido = 0
valor_total = 0 
valor_entrega = 0

print("Bem-vindo, meu nome e Davi Ribeiro")

#função para definir o valor conforme modelo
def escolha_modelo(valor_modelo):
	global pedido
	while True:
		modelo_escolhido = input("Qual modelo vai querer MCS/MLS/MCE/MLE? ")
		if modelo_escolhido not in modelos:
			print("modelo invalido, tente novamente")
			continue
		else:
			print(f"modelo: {modelo_escolhido}")
			pedido = float(valor_modelo[modelo_escolhido])
			return pedido

#função para calcular o desconto conforme quantidade
def num_camiseta():
#variaveis globais da função para resgatar no print main
	global valor_total
	global quantidade_desconto
	
	while True:
		try:
			quantidade = int(input("Digite uma quantidade: "))
			if quantidade > 20000: 					
				print("não é aceito pedidos nessa quantidade de camisetas;") 	
				continue
					 
			if 20 <= quantidade <= 199:
				desconto = 0.05
			elif 200 <= quantidade <= 1999:
				desconto = 0.07
			elif 2000 <= quantidade <= 20000:
				desconto = 0.12
			else:
				desconto = 0

			quantidade_desconto = (quantidade * (1 - desconto))
			valor_total = pedido * quantidade_desconto
			break
#caso entre com valor que não seja numero 
		except ValueError: 
			print("entre com o valor valido")

#função para calcular o frete 
def frete():
	global valor_entrega
	
	print("Qual forma de entrega? retirada na fabrica (0), transportadora (1), sedex (2)")

	while True:
		entrega =  int(input("Digita forma de entrega 0 , 1 ou 2: "))
		if entrega not in tipo_entrega:
			print("escolha uma opção valida")
			continue
		else:
			valor_entrega = float(tipo_entrega[entrega])
			return valor_entrega


escolha_modelo(valor_modelo)
num_camiseta()
frete()

#variavel para calcular o total do serviço com base nas globais
main = (f"valor total R$: {valor_total + valor_entrega:.2f}, valor unitario:{pedido} x (quantidade X desconto) = {quantidade_desconto} + {valor_entrega}")
print(main)