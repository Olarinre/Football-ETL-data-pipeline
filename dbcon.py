import psycopg2
import os
from dotenv import load_dotenv
from sqlmodel import Column, SQLModel, create_engine, Session, Field, Integer, String





class Tabledata(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    position: int = Field(sa_column=Column("position", Integer, nullable=False))
    team_name: str = Field(sa_column=Column("team_name", String, nullable=False))
    matches: int = Field(sa_column=Column("matches", Integer, nullable=False))
    points: int = Field(sa_column=Column("points", Integer, nullable=False))
    score_diff: int = Field(sa_column=Column("score_diff", Integer, nullable=False))
    goals: int = Field(sa_column=Column("goals", Integer, nullable=False))


load_dotenv
# Replace with your details
DATABASE_URL = f"postgresql+psycopg2://{os.getenv('username')}:Ayobami%40090499@{os.getenv('host')}/{os.getenv('db_name')}"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL logs


def get_session():
    with Session(engine) as session:
        print("✅ Database session created successfully.")
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)  # ✅ Creates the table(s) in PostgreSQL
    print("Tables created successfully.")

