from dotenv import load_dotenv
import psycopg2
import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session, Field





class Tabledata(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    team: str
    goals: int = 0


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

