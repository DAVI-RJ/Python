#cadastro e consulta de funcionarios

#menu para iniciar p sistema // servidor beckend
main = 	{   
	1: "Cadastrar Funcionário",
	2: {"nome": "Consultar Funcionário",
	 	"submenu": {
			1: "Consultar Todos",
			2: "Consultar por ID",
			3: "Consultar por Setor",
			4: "Voltar ao Menu"
		}
	 },
	3: "Remover Funcionário",
	4: "Encerrar Programa"
}
#painel ID global
id_RU = 5297807

#formatação da lista // banco de dados 
list_funcionario = []
    
#função para incrementar id + 1 conforme cadastro
def id_funcionario():
	if list_funcionario:	
		return list_funcionario[-1]["id"] + 1
	else:
		return id_RU 

# Menu principal, mosta opçoes sugeridas para consulta, e chama a funçao conforme digitado
# frontend
def menu_opcoes():
		print("\n ----- MENU PRINCIPAL -------")

		print("1 - Cadastrar Funcionário")
		print("2 - Consultar Funcionário")
		print("3 - Remover Funcionário")
		print("4 - Encerrar Programa")

		print("-" * 20)

		while True:
				try:
					opcao = int(input("\n Escolha uma opção: "))
					if opcao not in main:
							continue
					
					if opcao == 1:
							cadastro_fun()
							print("-" * 20)
				
					elif opcao == 2:
							consulta_fun()
							print("-" * 20)

					elif opcao == 3:
							remove_fun()
							print("-" * 20)
					
					elif opcao == 4:
							print("Programa encerrado.")
							break
																										
				except ValueError: 
					print("Opção inválida. Tente novamente.")

		return opcao

#cadastro novo funcionario 
def cadastro_fun():
		global id_RU
		print("-" * 20)
		print("------cadastro funcionário----")
		print("-" * 20)
		print(f"ID funcionario: {id_RU}")
		nome = input("qual e seu nome? ").upper()
		setor = input("qual e o setor: ").upper()
		salario = float(input("qual e o salario: "))
		
		new_id = id_funcionario()
		new_funcionario = {
			"id":new_id,
			"nome": nome,
			"setor": setor,
			"salario": salario,
			}
		
		list_funcionario.append(new_funcionario)
		print(f"Novo funcionario cadastrado com sucesso\n")
		print(f"Nome: {nome}")
		print(f"Setor: {setor}")
		print(f"Salario: {salario}")
		print("-" * 20)
		
		id_RU = new_id + 1		
		return id_RU , menu_opcoes()

#opcoes para consulta   // frontend
def consulta_fun(): 

	print("\n---- CONSULTA ---")

	print("1 - Consultar Todos")
	print("2 - Consultar por ID")
	print("3 - Consultar por Setor")
	print("4 - Voltar ao Menu")

	print("-" * 20)

	while True:
			try:
				opcao_consulta = int(input("\n Escolha uma opção: "))
				
				if opcao_consulta not in (main[2]["submenu"]):
						continue
				
				if opcao_consulta == 1:
					consultar_todos()
			
				elif opcao_consulta == 2:
					consultar_id()

				elif opcao_consulta == 3:
					consultar_setor()

				elif opcao_consulta == 4:
						menu_opcoes()
				else:
					print("Opção inválida.")

			except ValueError: 
				print("Opção inválida. Tente novamente.")
			
			#return opcao_consulta			


# consulta todos os funcionários
def consultar_todos():
	print("\n Lista de Funcionarios:")
	for fun in list_funcionario:
		print(fun)
	return consulta_fun()
					

# consulta funcionário por ID
def consultar_id():
	id_lista = int(input(" \n Digite o ID do funcionario: "))
	for fun in list_funcionario:
			if fun["id"] == id_lista:
					print("-" * 20)
					print(f"funcionario encontrado: {fun}")
			return consulta_fun()
	print("funcionario não encontrado.")


# Consulta por setor
def consultar_setor():
    setor = input(" \n Digite o setor: ").upper()
    encontrados = [fun for fun in list_funcionario if fun["setor"] == setor]
    
    if encontrados:
        print("\n Funcionarios encontrados:")
        for f in encontrados:
            print(f)
    else:
        print("\n Nenhum funcionario encontrado neste setor.")
		
    return consulta_fun()    

# Remove funcionário por ID
def remove_fun():
	id_excluir = int(input(" \n Digite o ID do funcionario para remover: "))
	for fun in list_funcionario:
			if fun["id"] == id_excluir:
					list_funcionario.remove(fun)
					print("-" * 20)
					print("funcionario removido com sucesso.")
					return menu_opcoes()
	print("Id inválido.")		
	

# Inicia o programa
print("Bem-vindo, meu nome e Davi Ribeiro")

menu_opcoes()