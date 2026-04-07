import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')

# Read from PostgreSQL
df = pd.read_sql('SELECT * FROM listings', engine)

# Save to CSV
df.to_csv('/Users/wasima/Documents/Finance/data/from_sql.csv', index=False)

print(f'Saved {len(df)} rows to data/from_sql.csv')
