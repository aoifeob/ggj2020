class AbilityCard:

    String animal;
    String abilityDescription;

    def __init__(animal):
        this.animal = animal
        this.abilityDescription = getDescription(animal)

    def getDescription(animal):
        if (animal == "rat"):
            return "Draw a new hand of 4 cards"
        elif(animal == "ox"):
            return "Add +4 to your current roll"
        elif(animal == "tiger"):
            return "Move an opponent's piece of choice back 4 spaces"
        elif(animal == "rabbit"):
            return "Double your current roll"
        elif(animal == "snake"):
            return "Add 2 cards from your opponent's hand to your own"
        elif(animal == "horse"):
            return "Your roll applies to 2 of your pieces this turn"
        elif(animal == "goat"):
            return "Make one unit permanently indestructible"
        elif(animal == "monkey"):
            return "Move a select allied unit forward to one space in front of the closest unit"
        elif(animal == "rooster"):
            return "Deploy an undeployed unit 4 spaces in addition to your normal move"
        elif(animal == "dog"):
            return "Move a select allied unit to one space behind the closest ally"
        elif(animal == "pig"):
            return "Choose 4 cards from your deck to be your next hand"

    def use():
        if (this.animal == "rat"):
            useRatCard()
        elif(this.animal == "ox"):
            useOxCard()
        elif(this.animal == "tiger"):
            useTigerCard()
        elif(this.animal == "rabbit"):
            useRabbitCard()
        elif(this.animal == "snake"):
            useSnakeCard()
        elif(this.animal == "horse"):
            useHorseCard()
        elif(this.animal == "goat"):
            useGoatCard()
        elif(this.animal == "monkey"):
            useMonkeyCard()
        elif(this.animal == "rooster"):
            useRoosterCard()
        elif(this.animal == "dog"):
            useDogCard()
        elif(this.animal == "pig"):
            usePigCard()

    def useRatCard():
        pass

    def useOxCard():
        pass

    def useTigerCard():
        pass

    def useRabbitCard():
        pass

    def useSnakeCard():
        pass

    def useHorseCard():
        pass

    def useGoatCard():
        pass

    def useMonkeyCard():
        pass

    def useRoosterCard():
        pass

    def useDogCard():
        pass

    def usePigCard():
        pass
