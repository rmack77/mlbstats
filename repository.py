import sqlite3

# Writes teams into database
def write_teams(teams):
    """Write teams to the database."""
    conn = sqlite3.connect('mlbstats.db')
    conn.execute('DELETE FROM team;')  # Clear existing teams
    cursor = conn.cursor()
    # Insert teams into the table
    for team in teams['teams']:
        cursor.execute('''
            INSERT INTO team (id, name, abbr, venue_id, venue_name, league_id, league_name, division_id, division_name)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''',
        (
            team['id'],
            team['name'],
            team['abbreviation'],
            team['venue']['id'],
            team['venue']['name'],
            team['league']['id'],
            team['league']['name'],
            team['division']['id'],
            team['division']['name']
            ))
    
    conn.commit()
    conn.close()
