from sqlalchemy import create_engine, Column, String, Boolean, Integer, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

db = create_engine("sqlite:///banco.db")

Base = declarative_base()

# criar classes
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String, nullable=False)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)
    admin = Column('admin', Boolean, default=False)
    
    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedido(Base):
    __tablename__ = "pedidos"
    
    STATUS_PEDIDOS = (
        ("PENDENTE", "PENDENTE"),
        ("CANCELADO", "CANCELADO"),
        ("FINALIZADO", "FINALIZADO")
    )
    
    id = Column('id', Integer, primary_key=True, autoincrement=True) 
    status = Column('status', ChoiceType(choices=STATUS_PEDIDOS)) # pendente, cancelado, finalizado 
    usuario = Column('usuario', ForeignKey("usuarios.id"))
    preco = Column('preco', Float)
    #itens =
    
    def __init__(self, usuario, status='PENDENTE', preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status
# itens pedidos
