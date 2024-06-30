from sklearn import svm

games_list = [
    "Fortnite", "Among Us", "Zelda", "League", "Elden Ring"
]

# Graphics, Multiplayer, Age, Difficulty, Price
games_score_list = [
    [4, 1, 5, 5, 0 ],
    [2, 1, 4, 2, 5.5 ],
    [7, 0, 2, 7, 6 ],
    [6, 1, 15, 7, 0 ],
    [9, 1, 1, 10, 6 ],
]

my_ideal_game = [9,1,1,9,0]
weights_list = [100,1,50,100,1]
recommendation_model = svm.SVC()
recommendation_model.fit(games_score_list, games_list,weights_list)
print(recommendation_model.predict([ my_ideal_game]))