from sqlmodel import SQLModel, create_engine, Session

from iam.config import Config

engine = create_engine(Config.DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
