import random
import time

club = ['Heart(♥)', 'Diamond(♦)','Club(♣)','Spades(♠)']
numbers = ['A','1','2','3','4','5','6','7','8','9','K','Q','J']
cardused = []
cardName , cardType = '', ''
cardValue = 0
playerCards = {}
dealerCards = {}
playerScore = 0
dealerScore = 0
isUserSurrender = False
lastHandId = 0
playerHands = {}

def drawCard(name):
    # Drawing random cards
    typeOfCard = random.choice(club)
    numberOnCard = random.choice(numbers)
    card = numberOnCard + typeOfCard
    if card in cardused:
        drawCard(name)
    else:
        cardused.append(card)
        assignValues(card,name)

def assignValues(card,name):
    # Assigning card values
    global cardName, cardValue
    cardName = card[0]
    if cardName.isnumeric():
        cardValue = int(cardName)
    else:
        if cardName == 'A':
            if name == 'player' and playerScore > 11:
                cardValue = 1
            elif name == 'dealer' and dealerScore > 11:
                cardValue = 1
                # print('dealersscore',cardValue)
            else:
                cardValue = 11
        else:
            cardValue = 10
    
    # Assigning card names
    global cardType
    cardType = card[1:]

def displayCard():
    global playerScore, dealerScore
    playerScore, dealerScore = 0,0
    print('-------------Displaying Cards---------------\n')
    print("Your cards : ", end="")
    for cards,value in playerCards.items():
        playerScore = playerScore + value
        print(" ",cards, end=" ,")
    print(f'\nYour Score : {playerScore}')

    print("\ndealer cards : ", end="")
    for cards,value in dealerCards.items():
        dealerScore = dealerScore + value
        print(" ",cards, end=" ,")
    print(f'\ndealer Score : {dealerScore} \n')

def getCardFor(name,variableName):
    drawCard(name)
    variableName[f'{cardName} of {cardType}'] = cardValue

def checkScores():
    if playerScore == 21 and dealerScore != 21:
            print(f"It's a BlackJack! You wins {bet*1.5}")
    elif dealerScore == 21 and playerScore != 21:
        print('Sorry! Dealer wins, Better luck next time')
    elif playerScore < 21 and dealerScore < 21:
        if dealerScore > playerScore :
            print('Sorry! Dealer wins, Better luck next time')
        elif playerScore == dealerScore:
            print('OOPS! Scores are Draw')
        else:
            print(f'Congratulations! You wins {bet}')
    elif playerScore < 21 and dealerScore > 21 :
        print(f'Congratulations! You wins {bet}')
    elif dealerScore < 21 and playerScore > 21 :
        print("Burst! Dealer wins, Better luck next time")
    elif dealerScore > 21 and playerScore > 21 :
        print('Sorry! Dealer wins, Better luck next time')
    elif playerScore == dealerScore:
        print('OOPS! Scores are Draw')
    if isUserSurrender:
        print(f'return amount {bet//2} ')


if __name__ == "__main__":
    print("1. Start \t 2. Exit")
    ch = int(input())
    while ch != 2:
        if ch == 1:
            bet = int(input("Enter Amount for Bet : \t")) 
            getCardFor('player',playerCards)
            getCardFor('player',playerCards)
            getCardFor('dealer',dealerCards)

            displayCard()
            inputString = '1. Hit \t 2. Stand   3. Double down   4. Surrender\n'

            plchoice = 2
            if playerScore != 21:
                plchoice = int(input(inputString))
            while plchoice != 2 :
                if plchoice == 1:
                    if playerScore != 21:
                        getCardFor('player',playerCards)
                        print('Drawing a Card for you....\n')
                        time.sleep(1)
                        displayCard()
                    if playerScore >= 21:
                        # Exiting becoz Playerscore exceded 21'
                        break
                elif plchoice == 2:
                    break
                elif plchoice == 3:
                    if len(playerCards) > 2 or len(playerCards) == 0:
                        print('Wrong Choice! Try Again')
                    else:
                        bet = bet * 2
                        getCardFor('player',playerCards)
                        print('Drawing a Card for you....\n')
                        time.sleep(1)
                        displayCard()
                        break
                elif plchoice == 4:
                    isUserSurrender = True
                    break
                    
                plchoice = int(input('1. Hit \t 2. Stand \n'))

            while dealerScore < 17:
                getCardFor('dealer',dealerCards)
                print('Dealer is drawing another Card....\n')
                time.sleep(2)
                displayCard()
                if playerScore > 21 or isUserSurrender:
                    # Exiting becoz Playerscore exceded 21'
                    break
            
            # Checking for scores
            checkScores()

        elif ch == 2:
            exit()
        else:
            print('Wrong Choice! Try Again')
        print("\nTo Play Again enter   1. Start \t 2. Exit")
        ch = int(input())

        # Resetting global variables 
        playerCards = {}
        dealerCards = {}
        cardused = []
        playerScore = 0
        dealerScore = 0
        isUserSurrender = False
