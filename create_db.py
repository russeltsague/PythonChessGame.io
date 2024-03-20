import os
import sqlite3

PATH_TO_DB = os.path.join(
    os.path.dirname(__file__),
    "db.chess"
)

create_player_match_table_query = "CREATE TABLE subject (won ENUM('Yes','No'), match_id INTERGER,player_id INTERGER, FOREIGN KEY(match_id) REFERENCES matchs(match_id),  FOREIGN KEY(player_id) REFERENCES players(player_id))"

create_players_table_query = """
CREATE TABLE players(name TEXT, location TEXT, game_won INTEGER, game_lost INETRGER, game_played INTERGER
players_id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT)
"""

create_matchs_table_query = "CREATE TABLE matchs(duration TIME, match_id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP)"

with sqlite3.connect(PATH_TO_DB) as connection:
    cursor = connection.cursor()

    for query in [create_player_match_table_query, create_players_table_query, create_match_table_query]:
        cursor.execute(query)    