# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

# Créez l'URL de connexion à la base de données
db_username = 'moussamar'
db_host = 'localhost'
db_name = 'friper_db'
db_url = f'postgresql://{db_username}@{db_host}/{db_name}'

# Créez le moteur SQLAlchemy
engine = create_engine(db_url)

# Créez une classe de session pour interagir avec la base de données
Session = sessionmaker(bind=engine)

# Créez les tables dans la base de données
Base.metadata.create_all(engine)
