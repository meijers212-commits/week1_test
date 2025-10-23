def create_card(rank:str,suite:str) -> dict:
    card_dict = {"rank": rank, "suite": suite}
    if rank == "a":
        card_dict["value"] = "14"
        return card_dict
    elif rank == "j" :
        card_dict["value"] = "11"
        return card_dict
    elif rank == "q":
        card_dict["value"] = "12"
        return card_dict
    elif rank =="k":
        card_dict["value"] = "13"
        return card_dict
    else:
        card_dict["value"] = rank
        return card_dict


def compare_cards(p1_card: dict, p2_card: dict)-> str:
    p1 = p1_card["value"]
    p2 = p2_card["value"]
    p1 = int(p1)
    p2 = int(p2)
    if p1 < p2:
        return "p2"
    if p1 > p2:
        return "p1"
    else:
        return "WAR"


def create_deck() -> list[dict]:
    suite = ["H", "C", "D", "S"]
    # ranks = ["J", "Q" , "K" , "A" ]
    decs = []

    for i in range(1 , 15):
        for j in suite:
            if i == 11:
                rank = "j"
                card = {"rank": rank , "suite":j , "value":i}
                decs.append(card)
            if i ==  12:
                rank = "q"
                card = {"rank": rank, "suite": j, "value": i}
                decs.append(card)
            if i == 13:
                rank = "k"
                card = {"rank": rank, "suite": j, "value": i}
                decs.append(card)
            if i ==  14:
                rank = "a"
                card = {"rank": rank, "suite": j, "value": i}
                decs.append(card)
        else:
            rank = i
            card = {"rank": rank, "suite": j, "value": i}
            decs.append(card)
    return decs

create_deck = create_deck()
import random


def shuffle(deck: list[dict]) -> list[dict]:
    deck = deck
    for i in range(1, 1001):
        num1 = random.randint(1 ,29)
        num2 = random.randint(1 ,29)
        if num1 == num2:
            continue
        else:
            deck[num1] , deck[num2] = deck[num2] , deck[num1]
    return deck

shuffle(create_deck)













