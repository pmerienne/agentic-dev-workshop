from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def init_db():
    SQLModel.metadata.create_all(engine)


def create_session():
    return Session(engine)
