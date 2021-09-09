import psycopg2

# Criando a conexão com o banco de dados

conn = psycopg2.connect(host="localhost", database="banco_de_teste", user="leonardo", password="1234")

# Abrindo um cursor para executar as operações
cur = conn.cursor()

# Executando as queries

cur.execute(
    """
        CREATE TABLE IF NOT EXISTS times (
            id BIGSERIAL PRIMARY KEY,
            nome_do_time VARCHAR NOT NULL,
            divisao VARCHAR(128) NOT NULL
        );
    """
)

cur.execute(
    """
        INSERT INTO times
            (nome_do_time, divisao)
        VALUES
            ('Zé do Leite FC', '1ª divisão'),
            ('Esporte Clube Estoura Dedo', '1ª divisão'),
            ('Atlético da esquina FC', '2ª divisão');
    """
)

cur.execute(
    """
        SELECT * FROM times;
    """
)

# Pegando a saída dos dados
registros = cur.fetchall()
print(registros)

# Persistindo as mudanças
conn.commit()

# Fechando a comunicação com o banco
cur.close()
conn.close()