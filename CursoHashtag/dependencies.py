from sqlalchemy import sessionmaker 
from models import db

def pegar_sessao():
    Session = sessionmaker(bind=db)
    session = Session()
    return session