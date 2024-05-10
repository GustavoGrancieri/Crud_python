import mysql.connector
try:
    
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '12345678',
        database = 'Loja'
    )
    if conexao.is_connected():
            print("Conexão bem-sucedida ao banco de dados")
            
    cursor = conexao.cursor()

    def adicionar():
        new_prod = input('Digite o nome do produto: ')
        new_value = float(input('Digite o valor do novo produto: '))
        comando = 'INSERT INTO vendas(prod, valor) VALUES(%s, %s)'
        dados = (new_prod, new_value)
        cursor.execute(comando, dados)
        conexao.commit()
        print('Produto adicionado com sucesso')
    
    def atualizar():
        op = input('Você deseja atualizar o nome, o valor ou ambos\n Digite a opção:')
        if op == 'nome':
            old_name = input('Digite o nome do produto a ser atualizado: ')
            new_name = input('Digite o novo nome do produto: ')
            comando = 'UPDATE vendas SET prod = %s WHERE prod = %s'
            dados = (new_name, old_name)
            cursor.execute(comando, dados)
            conexao.commit()
            print('Nome atualizado com sucesso')
        elif op == 'valor':
            name = input('Digite o nome do produto a ser atualizado o valor: ')
            new_value = float(input('Digite o novo valor do produto: '))
            comando = 'UPDATE vendas SET valor = %s WHERE prod = %s'
            dados = (new_value, name)
            cursor.execute(comando, dados)
            conexao.commit()
            print('Valor atualizado com sucesso')
        elif op == 'ambos':
            old_name = input('Digite o nome do produto a ser atualizado: ')
            new_name = input('Digite o novo nome do produto: ')
            new_value = float(input('Digite o novo valor do produto: '))
            comando = 'UPDATE vendas SET prod = %s, valor = %s WHERE prod = %s'
            dados = (new_name, new_value, old_name)
            cursor.execute(comando, dados)
            conexao.commit()
            print('Nome e valor atualizados com sucesso')
        else:
            print('Opção inválida...')
            
    def remover():
        rm_prod = input('Digite o nome do produto que deseja remover: ')
        comando = 'DELETE FROM vendas WHERE prod = %s'
        dados = (rm_prod,)
        cursor.execute(comando, dados)
        conexao.commit()
        print('Produto removido com sucesso')


    add_prod = input('Deseja adicionar, atualizar ou remover um produto?\n Qual a opção desejada: ')

    if add_prod == 'adicionar':
        adicionar()
        print('item adicionado com sucesso')

    elif add_prod == 'atualizar':
        atualizar()
        print('Item atualizado com sucesso')
        
    elif add_prod == 'remover':
        remover()
    
    else:
        print('opção inválida, reinicie o programa...')
        
except mysql.connector.Error as erro:
    print(f"Erro ao conectar ao banco de dados: {erro}")
    
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão com o banco de dados encerrada")

cursor.close()
conexao.close()