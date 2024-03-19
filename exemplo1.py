from sqlalchemy import create_engine

engine = create_engine('sqlite:///meubanco.db', echo=True)


print("Conexão com SQLite criada com sucesso!")