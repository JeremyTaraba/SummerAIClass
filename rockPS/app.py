
from flask import Flask, jsonify
from flask_cors import CORS
from sklearn import svm  

app = Flask(__name__)
CORS(app)

@app.route('/play/<user_move>', methods=['GET'])
def play(user_move):
    history = [1,1,3,2]

    model = svm.SVC()

    input_data = [  
        [1,1],
        [1,3],
        [3,2],
        [2,1]
    ]

    output_data = [3,2,1,1]

    model.fit(input_data, output_data)

    def compPlayer():
        data_record = [history[-2], history[-1]] # get the player's last two moves
        current = model.predict([data_record])[0] # determine it's next move

        # return the move that will beat the predicted move
        if current == 1:
            return 2
        elif current == 2:
            return 3
        else:
            return 1
        
    comp = compPlayer()
    user = int(user_move)
    comp_name = ""
    user_name = ""
    
    
        
    def getPlayer2():
        choice = int(input("Please select one of the following 1) Rock, 2) Paper, 3) Scissors: "))
        return choice


   

    if comp == 1 and user == 1:
        print("the computer chose rock")
        Result = "It's a tie!"
        # total_ties +=1
    elif comp == 1 and user == 2:
        print("the computer chose rock")
        Result = "The user wins!"
        # wins_player2 += 1
    elif comp == 1 and user == 3:
        print("the computer chose rock")
        Result = "The computer wins!"
        # wins_player1 += 1  
    elif comp == 2 and user == 1:
        print("the computer chose paper")
        Result = "The computer wins!"
        # wins_player1 += 1
    elif comp == 2 and user == 2:
        print("the computer chose paper")
        Result = "It's a tie!"
        # total_ties +=1
    elif comp == 2 and user == 3:
        print("the computer chose paper")
        Result = "The user wins!"
        # wins_player2 += 1
    elif comp == 3 and user == 1:
        print("the computer chose scissors")
        Result = "The user wins!"
        # wins_player2 += 1
    elif comp == 3 and user == 2:
        print("the computer chose scissors")
        Result = "The computer wins!"
        # wins_player1 += 1
    elif comp == 3 and user == 3:
        print("the computer chose scissors")
        Result = "It's a tie!!"
        # total_ties +=1
    
    if comp == 1:
        comp_name = "Rock"
    elif comp == 2:
        comp_name = "Paper"
    else:
        comp_name = "Scissors"
    
    if user == 1:
        user_name = "Rock"
    elif user == 2:
        user_name = "Paper"
    else:
        user_name = "Scissors"


    # if i != 4:
    #     print("Updating the training model...")
    #     history.append(user)

    #     input_data.append([history[-3], history[-2]])
    #     output_data.append(history[-1])

    #     model.fit(input_data,output_data)
    #     print("Finished updating the training model")
    message = "You played: " + user_name + " and the computer played: " + comp_name +" The result is : " + Result
    return jsonify(message)
            


        
    




if __name__ == '__main__':
    app.run(host="0.0.0.0")