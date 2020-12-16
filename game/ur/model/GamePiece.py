class GamePiece:

    int pieceId;
    int playerId;
    boolean isHome;
    boolean isOnBoard;
    Tile currentTile;

     def __init__(pieceId, playerId):
         this.pieceId = pieceId;
         this.playerId = playerId;
         this.isHome = false;
         this.isOnBoard = false;
