veiculos = [


    {"modelo": "Fusca", "codigo": "1990", "disponivel": True, "preco_diaria": 150},


    {"modelo": "Civic", "codigo": "2024", "disponivel": True, "preco_diaria": 900},


    {"modelo": "Camaro", "codigo": "2016", "disponivel": True, "preco_diaria": 1200},


    {"modelo": "Gol", "codigo": "2010", "disponivel": True, "preco_diaria": 500},
]


def listar_veiculos_disponiveis():
    
    """Lista os veículos disponíveis para aluguel."""  
    print("Veículos disponíveis para aluguel:")
    for veiculo in veiculos:
        if veiculo['disponivel']:
            
            print(
                f"Modelo: {veiculo['modelo']}, Ano: {veiculo.get('ano', 'N/A')}, Preço diária: R$ {veiculo.get('preco_diaria', 'N/A'):.2f}"
            )


def aluguel_veiculo():
    
    """Aluga um veículo."""
    
    modelo = input("Digite o modelo do veículo: ")
    
    for veiculo in veiculos:
        if veiculo['modelo'] == modelo:
            if veiculo['disponivel']:
                dias = int(input(f"Quantos dias de aluguel do {modelo}? "))
                total = dias * veiculo['preco_diaria']
                veiculo['disponivel'] = False
                print(f"Aluguel efetivado! Valor: R${total:.2f}")
                
                return
                
            else:
                print(f"Veículo {modelo} indisponível.")
                return
    print("Veículo {modelo} não encontrado.")


def devolucao_veiculo():

    codigo = input("Digite o código do veículo: ")
    
    for veiculo in veiculos:
        if veiculo['codigo'] == codigo:
            if not veiculo['disponivel']:
                veiculo['disponivel'] = True
                print("Veículo {veiculo['modelo']} devolvido!")
                
                return
                
    print("Veículo com o código {codigo} não encontrado.")


def menu():

    while True:
        print("Escolha a opção:")
        print("1. Listar Veículos")
        print("2. Alugar Veículo")
        print("3. Devolver Veículo")
        print("4. Sair")
        
        opcao = input(" número da opção desejada: ")
        
        if opcao == '1':
            listar_veiculos_disponiveis()
            
        elif opcao == '2':
            aluguel_veiculo()
            
        elif opcao == '3':
            devolucao_veiculo()
            
        elif opcao == '4':
            print("Saindo do sistema")
            
            break
            
        else:
            print("Opção inválida")
            input("Pressione Enter")


menu()