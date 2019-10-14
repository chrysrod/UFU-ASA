from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text, select, ForeignKey, exc

try:
    db = create_engine("postgresql_psycopg2://postgres:banco@192.168.99.100/base01")
    print(db)
    metadados = MetaData()
    alunos = Table('alunos', metadados, Column('id', Integer, primary_key=True), Column('nome', String(60)))
    metadados.create_all(db)
    insert_command = alunos.insert().values(nome = 'Francisco José Spindola')
    print(insert_command)
    conn = db.connect()
    conn.execute(insert_command)
except Exception as e:
    print(e)