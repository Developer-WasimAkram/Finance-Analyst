import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv('/Users/wasima/Documents/Finance/data/listings.csv')

# PostgreSQL connection
engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')

# Load to PostgreSQL
df.to_sql('listings', engine, if_exists='replace', index=False)