import GamePiece;
import BasicCard;
import random;

class Player:

    int playerId;
    List[] gamePieces;
    List[] deck;
    List[] abilities;
    booleanIsPlayer;
    boolean isComputer;
    boolean isWinner;

     def __init__(playerId, isPlayer):
         this.playerId = playerId;
         this.isWinner = false;
         this.isPlayer = isPlayer
         this.isComputer = !isPlayer
         this.gamePieces = initialilsePieces(playerId)
         this.deck = initialiseDeck
         this.abilities = initialiseAbilities(playerId)

    def initialilsePieces(playerId):
        list = [];
        for(int i=0;i<7;i++):
            list.append(GamePiece.__init__(i, playerId));

        return list;

    def initialiseDeck():
        list = [];
        for (int i=0;i<8;i++):
            list.append(BasicCard.__init__(false))

        for int(i=0;i<8;i++):
            list.append(BasicCard.__init__(true))

        for(ability in abilities):
            list.append(AbilityCard(ability))

        return random.shuffle(list);

    def initialiseAbilities(playerId):
        list = [];

        return list
