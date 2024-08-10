from sqlalchemy import create_engine, String, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

from werkzeug.security import generate_password_hash, check_password_hash

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
    senha: Mapped[str] = mapped_column(String(255))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f'Usuario({self.id}, {self.nome})'

    def define_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def verifica_senha(self, senha):
        return check_password_hash(self.senha, senha)

# String de conexão com o PostgreSQL
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# CRUD
def create_usuario(nome, senha, email, **kwargs):
    with Session(bind=engine) as session:
        usuario = Usuario(nome=nome, email=email, **kwargs)
        usuario.define_senha(senha)
        session.add(usuario)
        session.commit()

def read_usuario():
    with Session(bind=engine) as session:
        cmd_sql = select(Usuario)
        usuarios = session.execute(cmd_sql).fetchall()
        users = [user[0] for user in usuarios]
        return users

def read_user_by_id(id):
    with Session(bind=engine) as session:
        cmd_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(cmd_sql).fetchall()
        return usuario[0][0]

def update_user(id, **kwargs):
    with Session(bind=engine) as session:
        cmd_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(cmd_sql).scalar_one_or_none()
        if usuario is None:
            print('Usuario não encontrado')
        colunas = Usuario.__table__.columns.keys()
        for key, value in kwargs.items():
            if key in colunas:
                if key == 'senha':
                  usuario.define_senha(value)
                else:
                  setattr(usuario, key, value)
        session.commit()
        print('Usuário atualizado com sucesso')

if __name__ == '__main__':
    print('Adicionar Streamlit')
