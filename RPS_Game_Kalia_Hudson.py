import random
def generateNum(randomNumber):
    if randomNumber == 0 :
        return 'Rock'
    elif randomNumber == 1 :
        return 'Paper'
    elif randomNumber == 2 :
        return 'Scissors'
    else :
        print('Error, see code')
        
def whoWins(user,computer):
    if user == 'Rock' and computer == 'Scissors':
        return 'You win!!!'
    elif user == 'Rock' and computer == 'Paper':
        return 'You lose'
    elif user == 'Rock' and computer == 'Rock':
        return 'Its a draw'
    elif user == 'Paper' and computer == 'Rock':
        return 'You win!!!'
    elif user == 'Paper' and computer == 'Scissors':
        return 'You lose'
    elif user == 'Paper' and computer == 'Paper':
        return 'Its a draw'
    elif user == 'Scissors' and computer == 'Paper':
        return 'You win!!!'
    elif user == 'Scissors' and computer == 'Rock':
        return 'You lose'
    elif user == 'Scissors' and computer == 'Scissors':
        return 'Its a draw'
    else:
        print('Error, see code')

title = print('ROCK PAPER SCISSORS')
instructions = print('Enter R,P, or S for rock, paper, and scissors respectively')

for x in range(3) :
    randomNum = random.randint(0,2)
    roundCounter = x + 1;
    rounds = print('Round ', roundCounter , ': ')
    userAnswer = input('Enter your answer: ')
    computerChoice = generateNum(randomNum)
    if userAnswer == 'r' or userAnswer == 'R':
        user = 'Rock'
        winner = whoWins(user,computerChoice)
        print('Your Answer: ', user, '|| Computers Answer: ', computerChoice)
        print(winner)
    elif userAnswer == 'p' or userAnswer == 'P':
        user = 'Paper'
        winner = whoWins(user,computerChoice)
        print('Your Answer: ', user, '|| Computers Answer: ', computerChoice)
        print(winner)
    elif userAnswer == 's' or userAnswer == 'S':
        user = 'Scissors'
        winner = whoWins(user,computerChoice)
        print('Your Answer: ', user, '|| Computers Answer: ', computerChoice)
        print(winner)
    else :
        print('Please try again, Enter only R, P, or S')
    
    
    
        


