"""
Contains database configuration
"""

import os
# from dotenv import load_dotenv

# load_dotenv()

# DB_CONF = {
#     "host": os.getenv("PGHOST"),
#     "port": int(os.getenv("PGPORT", 5432)),
#     "dbname": os.getenv("PGDATABASE"),
#     "user": os.getenv("PGUSER"),
#     "password": os.getenv("PGPASSWORD"),
# }

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:allcowseatgrass@localhost:5432/library-management-db")

