from game import Game
from connection import Connection

class GameDao():

    #Data Access Object

    __SELECT = 'SELECT * FROM games ORDER BY id'
    __SELECT_ID = 'SELECT * FROM games WHERE id = ?'
    __INSERT = 'INSERT INTO games (name, price, rate) VALUES (?, ?, ?)'
    __DELETE = 'DELETE FROM games WHERE id = ?'
    __UPDATE = 'UPDATE games SET name=?, price=?, rate=? WHERE id=?'

    @classmethod
    def select_id(cls, game):
        try:
            cursor = Connection.getCursor()
            value = (game.game_id,)
            cursor.execute(cls.__SELECT_ID, value)
            dataGet = cursor.fetchone()
            return dataGet

        except Exception as error:
            print(f'Error getting the data: {error}')

    @classmethod
    def select(cls):
        cursor = Connection.getCursor()
        cursor.execute(cls.__SELECT)
        dataGet = cursor.fetchall()
        games = []

        for data in dataGet:
            game = Game(data[0], data[1], data[2], data[3])
            games.append(game)
        Connection.close()
        return games

    @classmethod
    def insert(cls, game):
        try:
            connection = Connection.getConnection()
            cursor = Connection.getCursor()
            print(f'Data to insert: {game}')
            values = (game.name, game.price, game.rate)
            cursor.execute(cls.__INSERT, values)
            connection.commit()
            return cursor.rowcount

        except Exception as error:
            connection.rollback()
            print(f'Error inserting data to database: {error}')

        finally:
            Connection.close()

    @classmethod
    def update(cls, game):
        try:
            connection = Connection.getConnection()
            cursor = Connection.getCursor()
            print(f'Data to update: {game}')
            values = (game.name, game.price, game.rate, game.game_id)
            cursor.execute(cls.__UPDATE, values)
            connection.commit()
            return cursor.rowcount

        except Exception as error:
            connection.rollback()
            print(f'Error updating data: {error}')

        finally:
            Connection.close()

    @classmethod
    def delete(cls, game):
        try:
            connection = Connection.getConnection()
            cursor = Connection.getCursor()
            print(f'Data to delete: {game}')
            value = (game.game_id,)
            cursor.execute(cls.__DELETE, value)
            connection.commit()
            return cursor.rowcount

        except Exception as error:
            connection.rollback()
            print(f'Error deleting data: {error}')

        finally:
            Connection.close()
        

#if __name__ == "__main__":
    #Code to GET an element by id
    #game = Game(game_id=3)
    #gottengame = GameDao.select_id(game)
    #print(gottengame)


    #Code to READ database
    #games = GameDao.select()
    #for game in games:
    #    print(game)

    #Code to INSERT new data
    #game = Game(name='Fifa 21', price='25', rate='9.5')
    #newData = GameDao.insert(game)
    #print(f'Data inserted: {newData}')

    #Code to UPDATE data
    #game = Game(2, 'Call of Duty 1', '25', '9.8')
    #dataUpdate = GameDao.update(game)
    #print(f'Data updated: {dataUpdate}')

    #Code to DELETE data
    #game = Game(game_id=2)
    #dataDelete = GameDao.delete(game)
    #print(f'Data deleted: {dataDelete}')
