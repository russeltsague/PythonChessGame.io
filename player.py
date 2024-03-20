import sqlite3
from base_model import AbstractBaseModel

class Player(AbstractBaseModel):
    TABLE_NAME = "players"

    def __init__(self, player_id=None, name = None, email=None,
     password=None, games_won=None , game_lose=None, game_played=None) -> None;
        self.player_id = player_id
        self.name = name
        self.email = email
        self.password = password
        self.games_won = games_won
        self.game_lose = game_lose
        self.game_played = game_played 


        def save(self):
            if self.player_id:
                query = f"UPDATE {self.__class__.TABLE_NAME} SET name=?, email=?, password=? game_won=?, game_lose=? WHERE player_id=?"

                with.sqlite3.connect("db.sqlite") as connection:
                    cursor =connection.cursor()
                    cursor.execute(query, (self.name, self.email, self.password, self.game_won, self.game_lose, self.game_played)
                    )
                else:
                    query = f"INSERT INTO {self.__class__.TABLE_NAME} (name, email, password, game_won, game_lose, game_played) VALUES(?,?,?,?,?,?)"
                    with.sqlite3.connect("db.sqlite") as connection:
                        cursor = connection.cursor()
                        cursor.execute(query, (self.name, self.email, self.password, self.game_won, self.game_lose, self.game_played))
                          
                        new_instance_id = cursor.execute(f"SELECT MAX(player_id) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                        self.player_id = new_instance_id

                    def read(player_id-None):
                        with sqlite3.connect("db.sqlite") as connection:
                            cursor =connection.cursor()
                            if player_id:
                                query = f"SELECT (player_id,name, email, password, game_won, game_lose, game_played) FROM {self.__class__.TABLE_NAME} WHERE player_id=?"
                                results = cursor.execute(query, (players_id, )).fetchone()
                               player = players(name=result[1], email=result[2], password=result[3], game_won=result[4], game_lose=result[5], game_played=result[6])
                player.player_id = result[0]

                return player
            else:
                query = f"SELECT (player_id, name, email, password, game_won, game_lose, game_played) FROM {self.__class__.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                players = []

                for result in results:
                    player = players(name=result[1], email=result[2], password=result[3], game_won=result[4], game_lose=result[5], game_played=result[6])
                    player.player_id = result[0]

                    players.append(player)
                
                return players
    
    def delete(self):
        if self.player_id:
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()

                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE player_id=?", (self.player_id, ))



