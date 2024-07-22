
from flask import Flask, jsonify, request
from flask_cors import CORS
from sklearn import svm  

app = Flask(__name__)
CORS(app)

history = [1,1,3,2]

input_data = [  
        [1,1],
        [1,3],
        [3,2],
        [2,1]
    ]

output_data = [3,2,1,1]

num_player_wins = 0
num_comp_wins = 0
num_ties = 0

@app.route('/play', methods=['POST'])
def play():
  
    global num_player_wins, num_comp_wins, num_ties
    model = svm.SVC()

    

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
    user = request.json.get("move")
    comp_name = ""
    user_name = ""


   

    if comp == 1 and user == 1:
        print("the computer chose rock")
        Result = "It's a tie!"
        num_ties +=1
    elif comp == 1 and user == 2:
        print("the computer chose rock")
        Result = "The user wins!"
        num_player_wins += 1
    elif comp == 1 and user == 3:
        print("the computer chose rock")
        Result = "The computer wins!"
        num_comp_wins += 1  
    elif comp == 2 and user == 1:
        print("the computer chose paper")
        Result = "The computer wins!"
        num_comp_wins += 1
    elif comp == 2 and user == 2:
        print("the computer chose paper")
        Result = "It's a tie!"
        num_ties +=1
    elif comp == 2 and user == 3:
        print("the computer chose paper")
        Result = "The user wins!"
        num_player_wins += 1
    elif comp == 3 and user == 1:
        print("the computer chose scissors")
        Result = "The user wins!"
        num_player_wins += 1
    elif comp == 3 and user == 2:
        print("the computer chose scissors")
        Result = "The computer wins!"
        num_comp_wins += 1
    elif comp == 3 and user == 3:
        print("the computer chose scissors")
        Result = "It's a tie!!"
        num_ties +=1
    
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

    history.append(user)
    input_data.append([history[-3], history[-2]])
    output_data.append(history[-1])
   
    return jsonify({
      "player_move": user_name,
      "computer_move": comp_name,
      "result": Result,
      "num_player_wins": num_player_wins,
      "num_comp_wins": num_comp_wins,
      "num_ties": num_ties
  })
            


        
@app.route("/reset", methods=["POST"])
def game_reset():
    global num_player_wins, num_comp_wins, num_ties
    num_player_wins = 0
    num_comp_wins = 0
    num_ties = 0

    return jsonify({
      "num_player_wins": num_player_wins,
      "num_comp_wins": num_comp_wins,
      "num_ties": num_ties
  })



if __name__ == '__main__':
    app.run(host="0.0.0.0")