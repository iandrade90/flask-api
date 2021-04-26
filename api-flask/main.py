from flask import Flask, jsonify, request
from connection import Connection
from game import Game
from gameDao import GameDao

app = Flask(__name__)

@app.route('/games/<id>', methods=['GET'])
def get_games_id(id):
    game = Game(game_id=id)
    idgame = GameDao.select_id(game)
    
    return jsonify(idgame)



if __name__ == "__main__":
    app.run(debug=False)
