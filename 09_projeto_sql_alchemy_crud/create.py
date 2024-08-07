from sqlalchemy import create_engine, String, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# Detalhes da conexão com o PostgreSQL
POSTGRES_USER = 'admin'
POSTGRES_PASSWORD = '12345'
POSTGRES_DB = 'bd_usuarios'
POSTGRES_HOST = 'postgres'  # Nome do serviço PostgreSQL
POSTGRES_PORT = '5432'

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f'Usuario({self.id}, {self.nome})'

# String de conexão com o PostgreSQL
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# CRUD
def create_usuario(nome, senha, email, **kwargs):
    with Session(bind=engine) as session:
        usuario = Usuario(nome=nome, email=email, senha=senha, **kwargs)
        session.add(usuario)
        session.commit()

if __name__ == '__main__':
    create_usuario('Batman', '123', 'batman@mail.com')

