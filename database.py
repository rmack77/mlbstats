import sqlite3

FILE = 'mlbstats.db'

# MLB STAT Database Initialization Script
def initialize_database():
    print("Initializing the MLB stat database...")
    does_file_exists = file_exists(FILE)
    if (not does_file_exists):
        print("Database file does not exist. Creating a new database...")
        create_database(FILE)
    else:
        print("Database file already exists. Checking version...")
    dbversion = get_database_version(FILE)
    print(f"Current database version: {dbversion}")
    perform_version_migration(FILE, dbversion)

# Checks to see if a file exists
def file_exists(filename):
    """Check if a file exists."""
    try:
        with open(filename, 'r'):
            return True
    except FileNotFoundError:
        return False

# Initialize the database with tables
def create_database(filename):
    """Initialize the database with some sample data."""
    conn = sqlite3.connect(filename)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS team
        (
              id INTEGER PRIMARY KEY
            , name TEXT
            , abbr TEXT
            , venue_id INTEGER
            , venue_name TEXT
            , league_id INTEGER
            , league_name TEXT
            , division_id INTEGER
            , division_name TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS dbversion
        (
            version TEXT
        )
    ''')
    conn.execute('''INSERT INTO dbversion (version) VALUES ('1.01')''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Perform version migration if necessary
def perform_version_migration(filename, start_version):
    """Perform version migration if necessary."""
    print("Migration not necessary.")

# Get the current database version
def get_database_version(filename):
    """Get the current database version."""
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute('SELECT version FROM dbversion')
    version = cursor.fetchone()
    if version:
        return version[0]
    else:
        return None


