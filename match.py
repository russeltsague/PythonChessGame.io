import sqlite3

class Match:
    TABLE_NAME = "matchs"

    def __init__(self, match_id=None, time=None, duration=None) -> None:
        self.match_id = match_id
        self.time = time
        self.duration = duration

    def save(self):
        if self.match_id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET time=?, duration=? WHERE match_id=?"

            with sqlite3.connect("db.chess") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.time, self.duration, self.match_id))
        else:
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (time, duration) VALUES(?,?)"
            with sqlite3.connect("db.chess") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.time, self.duration))

                new_instance_id = cursor.execute(f"SELECT MAX(id) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.match_id = new_instance_id

    def read(match_id=None):
        with sqlite3.connect("db.chess") as connection:
            cursor = connection.cursor()
            if match_id:
                query = f"SELECT (match_id, time, duration) FROM {self.__class__.TABLE_NAME} WHERE match_id=?"

                result = cursor.execute(query, (match_id, )).fetchone()

                matchs = match(time=result[1], duration=result[2])
                matchs.match_id = result[0]

                return matchs
            else:
                query = f"SELECT (match_id, time, duration) FROM {self.__class__.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                matchs = []

                for result in results:
                    matchs = match(time=result[1], duration=result[2])
                    matchs.match_id = result[0]

                    matchs.append(matchs)
                
                return matchs
    
    def update(self):
        if self.match_id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET time=?, duration=? WHERE match_id=?"

            with chess.connect("db.chess") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.time, self.duration, self.match_id))
 def delete(self):
        if self.match_id:
            with chess.connect("db.chess") as connection:
                cursor = connection.cursor()

                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE match_id=?", (self.match_id, ))