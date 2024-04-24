from chess.Backend.controller.configurations import *
from chess.Frontend.models import model
from chess.Backend.View import piece



class Controller():
	
    def __init__(self):
        self.init_model()

    def init_model(self): 
		# instantiated a new Model class within controller class
		# A way of controller to interact with model
        self.model = model.Model()

	# wrapper around function in piece class 
    def get_numeric_notation(self, position):
        return piece.get_numeric_notation(position)

	# wrapper around functions in model class
    def get_all_pieces_on_chess_board(self):
        return self.model.items()

    def reset_game_data(self):
        self.model.reset_game_data()

    def reset_to_initial_locations(self):
        self.model.reset_to_initial_locations()

    def get_alphanumeric_position(self, rowcol):
    	return self.model.get_alphanumeric_position(rowcol)

    def get_piece_at(self, position_of_click):
    	return self.model.get_piece_at(position_of_click)

    def pre_move_validation(self, start_pos, end_pos):
    	return self.model.pre_move_validation(start_pos, end_pos)

    def player_turn(self):
    	return self.model.player_turn

    def moves_available(self, position):
    	return self.model.moves_available(position)