# class to handle all errors and exceptions

class ChessError(Exception): pass # inherits from the standard Exception class
# Exceptions if the game rules are not being followed or in verdict cases
class Check(ChessError): pass
class InvalidMove(ChessError): pass
class CheckMate(ChessError): pass
class Draw(ChessError): pass
class NotYourTurn(ChessError): pass
class InvalidCoord(ChessError): pass