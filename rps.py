import random
from sklearn import svm  
import time
history = [1,1,3,2]

input_data = [  
	[1,1],
	[1,3],
	[3,2],
	[2,1]
]

output_data = [3,2,1,1]

model = svm.SVC()
model.fit(input_data, output_data)

def getPlayer1():
	data_record = [history[-2], history[-1]] # get the player's last two moves
	current = model.predict([data_record])[0] # determine it's next move

	# return the move that will beat the predicted move
	if current == 1:
		return 2
	elif current == 2:
		return 3
	else:
		return 1
     
def getPlayer2():
	choice = int(input("Please select one of the following 1) Rock, 2) Paper, 3) Scissors: "))
	return choice

wins_player1 = 0
wins_player2 = 0
total_ties = 0

for i in range(5):
    print("Game", i+1)
    time.sleep(.5)
    comp = getPlayer1()
    user = getPlayer2()

    time.sleep(.5)
    if comp == 1 and user == 1:
        print("the computer chose rock")
        time.sleep(.5)
        print("It's a tie!")
        total_ties +=1
        time.sleep(.5)
    elif comp == 1 and user == 2:
        print("the computer chose rock")
        time.sleep(.5)
        print("The user wins!")
        wins_player2 += 1
        time.sleep(.5)
    elif comp == 1 and user == 3:
        print("the computer chose rock")
        time.sleep(.5)
        print("The computer wins!")
        wins_player1 += 1 
        time.sleep(.5)  
    elif comp == 2 and user == 1:
        print("the computer chose paper")
        time.sleep(.5)
        print("The computer wins!")
        wins_player1 += 1
        time.sleep(.5)
    elif comp == 2 and user == 2:
        print("the computer chose paper")
        time.sleep(.5)
        print("It's a tie!")
        total_ties +=1
        time.sleep(.5)
    elif comp == 2 and user == 3:
        print("the computer chose paper")
        time.sleep(.5)
        print("The user wins!")
        wins_player2 += 1
        time.sleep(.5)
    elif comp == 3 and user == 1:
        print("the computer chose scissors")
        time.sleep(.5)
        print("The user wins!")
        wins_player2 += 1
        time.sleep(.5)
    elif comp == 3 and user == 2:
        print("the computer chose scissors")
        time.sleep(.5)
        print("The computer wins!")
        wins_player1 += 1
        time.sleep(.5)
    elif comp == 3 and user == 3:
        print("the computer chose scissors")
        time.sleep(.5)
        print("It's a tie!!")
        total_ties +=1
        time.sleep(.5)

    if i != 4:
        print("Updating the training model...")
        history.append(user)

        input_data.append([history[-3], history[-2]])
        output_data.append(history[-1])

        model.fit(input_data,output_data)
        print("Finished updating the training model")

print("Final Results:")
time.sleep(.5)
print("Computer: ", wins_player1)
time.sleep(.5)
print("Player: ", wins_player2)
time.sleep(.5)
print("Total ties: ", total_ties)
time.sleep(.5)