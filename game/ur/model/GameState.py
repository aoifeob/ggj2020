import Player;
import Board;

class GameState:

    boolean hasWinner;
    Player playerCharacter;
    Player computer;
    Board board;

     def __init__():
         this.hasWinner = false;
         this.playerCharacter = Player.__init__(1, true)
         this.computer = Player.__init__(2, false)
         this.board = Board.__init__()
