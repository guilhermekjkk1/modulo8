import csv
import os

# Listas globais para armazenar usuários e produtos
usuarios = []
produtos = []

# Funções de manipulação de arquivos
def carregar_usuarios():
    global usuarios
    try:
        with open('usuarios.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            usuarios = [linha for linha in reader]
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")

def salvar_usuarios():
    with open('usuarios.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['nome', 'senha', 'nivel']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(usuarios)

def carregar_produtos():
    global produtos
    try:
        with open('produtos.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            produtos = [linha for linha in reader]
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")

def salvar_produtos():
    with open('produtos.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['codigo', 'nome', 'preco', 'quantidade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produtos)

# CRUD de Usuários
def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    nivel = input("Digite o nível do usuário (admin/funcionario): ")
    usuarios.append({'nome': nome, 'senha': senha, 'nivel': nivel})
    salvar_usuarios()
    print("Usuário criado com sucesso!")

def listar_usuarios():
    print("Usuários cadastrados:")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Nível: {usuario['nivel']}")

def editar_usuario():
    nome = input("Digite o nome do usuário que deseja editar: ")
    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f"Editando usuário {usuario['nome']}")
            usuario['nome'] = input("Novo nome: ")
            usuario['senha'] = input("Nova senha: ")
            usuario['nivel'] = input("Novo nível: ")
            salvar_usuarios()
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado!")

def deletar_usuario():
    nome = input("Digite o nome do usuário que deseja remover: ")
    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuarios.remove(usuario)
            salvar_usuarios()
            print("Usuário removido com sucesso!")
            return
    print("Usuário não encontrado!")

# CRUD de Produtos
def criar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    produtos.append({'codigo': codigo, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
    salvar_produtos()
    print("Produto criado com sucesso!")

def listar_produtos():
    print("Produtos cadastrados:")
    for produto in produtos:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def editar_produto():
    codigo = input("Digite o código do produto que deseja editar: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"Editando produto {produto['nome']}")
            produto['nome'] = input("Novo nome: ")
            produto['preco'] = float(input("Novo preço: "))
            produto['quantidade'] = int(input("Nova quantidade: "))
            salvar_produtos()
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado!")

def deletar_produto():
    codigo = input("Digite o código do produto que deseja remover: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)
            salvar_produtos()
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado!")

# Funcionalidade extra: busca de produtos
def buscar_produto():
    nome = input("Digite o nome do produto que deseja buscar: ")
    for produto in produtos:
        if produto['nome'] == nome:
            print(f"Produto encontrado: Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
            return
    print("Produto não encontrado!")

# Funcionalidades de ordenação de produtos
def listar_produtos_ordenados_nome():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    print("Produtos ordenados por nome:")
    for produto in produtos_ordenados:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def listar_produtos_ordenados_preco():
    produtos_ordenados = sorted(produtos, key=lambda x: float(x['preco']))
    print("Produtos ordenados por preço:")
    for produto in produtos_ordenados:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

# Função de login com controle de permissões
def login():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    for usuario in usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha:
            print(f"Bem-vindo, {nome}!")
            return usuario['nivel']
    
    print("Usuário ou senha incorretos.")
    return None

# Função principal
def main():
    carregar_usuarios()
    carregar_produtos()

    while True:
        nivel = login()
        if nivel:
            break

    while True:
        if nivel == 'admin':
            print("Menu Admin")
            print("1. Cadastrar usuário")
            print("2. Listar usuários")
            print("3. Editar usuário")
            print("4. Deletar usuário")
            print("5. Cadastrar produto")
            print("6. Listar produtos")
            print("7. Editar produto")
            print("8. Deletar produto")
            print("9. Buscar produto")
            print("10. Listar produtos ordenados por nome")
            print("11. Listar produtos ordenados por preço")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                criar_usuario()
            elif opcao == '2':
                listar_usuarios()
            elif opcao == '3':
                editar_usuario()
            elif opcao == '4':
                deletar_usuario()
            elif opcao == '5':
                criar_produto()
            elif opcao == '6':
                listar_produtos()
            elif opcao == '7':
                editar_produto()
            elif opcao == '8':
                deletar_produto()
            elif opcao == '9':
                buscar_produto()
            elif opcao == '10':
                listar_produtos_ordenados_nome()
            elif opcao == '11':
                listar_produtos_ordenados_preco()
            elif opcao == '0':
                break
            else:
                print("Opção inválida!")
        else:
            print("Menu Funcionário")
            print("1. Listar produtos")
            print("2. Buscar produto")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                listar_produtos()
            elif opcao == '2':
                buscar_produto()
            elif opcao == '0':
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    main()
