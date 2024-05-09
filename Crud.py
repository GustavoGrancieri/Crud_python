import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345678',
    database = 'Loja'
)

cursor = conexao.cursor()

add_prod = input('Deseja adicionar, atualizar ou remover um produto?\n Qual a opção desejada: ')

if add_prod == 'adicionar':
    new_prod = input('Digite o nome do produto: ')
    new_value = float(input('Digite o valor do novo produto: '))
    comando = f'INSERT INTO vendas(prod, valor) VALUES("{new_prod}", {new_value})'
    cursor.execute(comando)
    conexao.commit()
    print('item adicionado com sucesso')

elif add_prod == 'atualizar':
    op = input('Você deseja atualizar o nome, o valor ou ambos\n Digite a opção:')
    if op == 'nome':
        old_name = input('Digite o nome do produto a ser atualizado: ')
        new_name = input('Digite o novo nome do produto: ')
        comando = f'UPDATE vendas SET prod = "{new_name}" WHERE prod = "{old_name}"'
        cursor.execute(comando)
        conexao.commit()
        print('nome atualizado com sucesso')
    elif op == 'valor':
        name = input('Digite o nome do produto a ser atualizado o valor: ')
        new_value = float(input('Digite o novo valor do produto: '))
        comando = f'UPDATE vendas SET valor = {new_value} WHERE prod = "{name}"'
        cursor.execute(comando)
        conexao.commit()
        print('valor atualizado com sucesso')
    elif op == 'ambos':
        old_name = input('Digite o nome do produto a ser atualizado: ')
        new_name = input('Digite o novo nome do produto: ')
        new_value = float(input('Digite o novo valor do produto: '))
        comando = f'UPDATE vendas SET valor = {new_value}, prod = "{new_name}" WHERE prod = "{old_name}"'
        print('nome e valor atualizado com sucesso')
        cursor.execute(comando)
        conexao.commit()
    else:
        print('opção inválida...')
elif add_prod == 'remover':
    rm_prod = input('Digite o nome do produto que deseja remover: ')
    comando = f'DELETE  FROM vendas WHERE prod = "{rm_prod}"'   
    print('Item deletado com sucesso')  
    cursor.execute(comando)
    conexao.commit()
    
else:
    print('opção inválida, reinicie o programa...')

cursor.close()
conexao.close()