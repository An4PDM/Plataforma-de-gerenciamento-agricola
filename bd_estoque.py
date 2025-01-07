import mysql.connector

bd = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '16092005Dn!',
    database = 'estoque'
)

cursor = bd.cursor()

# Gerenciamento de produtos
def gerenciar_produtos (acao,id,n,e):
    if acao == '+':
        q = '''INSERT INTO produto VALUES (%s,%s,%s);'''
        cursor.execute(q,(id,n,e))
        bd.commit()
        return 'Produto adicionado com sucesso.'
    
    elif acao == '-':
        q = '''DELETE FROM produto WHERE idP = %s;'''
        cursor.execute(q,(id,))
        bd.commit()
        return 'Produto deletado com sucesso.'
    
    elif acao == 'Editar':
        q = '''UPDATE produto SET nome = %s,
                                    estoque_minimo = %s
                                    WHERE idP = %s;'''
        cursor.execute(q,(n,e,id))
        bd.commit()
        return 'Atualização feita com sucesso.'
    
def gerenciar_equipamentos (acao,id,n,s):
    if acao == '+':
        q = 'INSERT INTO equipamento VALUES (%s,%s,%s);'
        cursor.execute(q,(id,n,s))
        bd.commit()
        return 'Equipamento adicionado com sucesso.'
    
    elif acao == '-':
        q = 'DELETE FROM equipamento WHERE idE = %s;'
        cursor.execute(q,(id))
        bd.commit()
        return 'Atualização feita com sucesso.'
    
    elif acao == 'Editar':
        q = '''UPDATE equipamento SET nome = %s,
                                        status = %s
                                        WHERE idE = %s;'''
        cursor.execute(q,(n,s,id))
        bd.commit()
        return 'Atualização feita com sucesso.'
    
def gerenciar_marcas (n):
    q = 'INSERT INTO marca (nome) VALUES (%s);'
    cursor.execute(q,((n,)))
    bd.commit()
    print('BUCETOIDES')


    



