from utils.deck import shuffle
from utils.deck import create_deck


def create_player(name:str) -> dict:
    if name =="":
        name = "AI"
    player_dic = {"name": name , "hand" :[] , "won_pile":[]}
    return player_dic


def init_game()->dict:
    pl1 = create_player("moshe")
    pl2 = create_player("")

    card_ls = shuffle(create_deck)
    pl1["hand"].append(card_ls[1:15])
    pl2["hand"].append(card_ls[15:30])

    game_dic = { "deck": card_ls ,
                 "player_1" : pl1,
                 "player_2": pl2 }
    return game_dic

players = init_game()
pla1 = players["player_1"]
pla2 = players["player_2"]
ca = players["deck"]



def play_round(player_1: dict, player_2: dict)-> None:
    player1_hand = player_1['hand'].pop()
    player2_hand = player_2['hand'].pop()


play_round(pla1, pla2)



if __name__ == "__main__":
    init_game()



