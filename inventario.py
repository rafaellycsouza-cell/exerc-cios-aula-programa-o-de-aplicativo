estoque = {'sabão em pó': [100,20.00],
            'detergente': [70,10.50], 
            'amaciante': [90,50.00], 
            'lustra móveis': [64, 30.50]}
historico_vendas = []

def cadastrar_produtos (nome, quantidade, preco):
    if nome in estoque:
        print(f"Produto já cadastrado")
    else:
        estoque[nome] = [quantidade, preco]
        print("Produto cadastrado com sucesso!")
    