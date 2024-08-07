import random
import time


# To make file
def dice_double():
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    roll_total = roll_1 + roll_2
    return roll_total


def bidding(x):
    Bidders_Dict = {}
    for k in players:  # Dictionary of players who are bidding
        player_data = player_info[k]
        a = {k: player_data}
        Bidders_Dict.update(a)
    keys=list(Bidders_Dict.keys())
    bidders = len(players)

    if bidders == 1:
        player_1 = keys[0]
        bidders_1 = Bidders_Dict[player_1]
        print(Bidders_Dict[player_1][1], "Won")
        print("Thanks for playing")  # Add exit from the loop

    elif bidders == 2:
        player_1 = keys[0]
        player_2 = keys[1]
        bidders_1 = Bidders_Dict[player_1]
        bidders_2 = Bidders_Dict[player_2]
        property = x
        print("Auction is for", property)
        last_Bidder = 'To Solve Error'  # Will take the bidder 1 and 2 index wise
        Final_Price = 0
        prop_number = 0
        for x in range(1, 41):
            if board_info[x][0] == property:
                prop_number += x
                break
        Base_price = board_info[prop_number][2]
        Bidder_1, Bidder_2 = 0, 0
        flag, c = 0, 0
        Bid = ''
        print(Bidders_Dict[player_1][1], "should write", Bidders_Dict[player_1][5], 'to bid and ',
              Bidders_Dict[player_2][1], " should write ", Bidders_Dict[player_2][5], "To Bid")
        print("Press 'Enter' to stop bidding")
        while True:
            Bid = input("Enter initial to bid")
            if Bid != Bidders_Dict[player_1][5] and Bid != Bidders_Dict[player_2][5] and Bid != '':
                print("Enter Valid input")
                continue
            if Bid == last_Bidder:
                print("You can't bid on yourself")
                continue  # Checked if same person didn't rebid
            c += 1  # Won't Add when Wrong bid is placed
            Current_Bid = int(Base_price) + 5 * c
            if Bid == Bidders_Dict[player_1][5]:
                if Bidders_Dict[player_1][3] > Current_Bid:
                    Bidder_1 = Current_Bid  # theek karje
                    # Current_Bid = int(Base_price) + 5 * c
                else:
                    print("You don't have enough funds")
                    Current_Bid = Current_Bid - 5
                    last_Bidder = Bidders_Dict[player_2][5]
                    print("Property goes to", last_Bidder, "for", Final_Price)
                    break
            if Bid == Bidders_Dict[player_2][5]:
                if Bidders_Dict[player_2][3] > Current_Bid:
                    Bidder_2 = Current_Bid
                else:
                    print("You don't have enough funds")
                    Current_Bid = Current_Bid - 5
                    last_Bidder = Bidders_Dict[player_1][5]
                    print("Property goes to", last_Bidder, "for", Final_Price)
                    break
            if Bid == '':
                print("Property goes to", last_Bidder, "for", Final_Price)
                break

            if Bid == Bidders_Dict[player_1][5] or Bid == Bidders_Dict[player_2][5]:
                last_Bidder = Bid

            if Bidder_1 > Bidder_2:
                Final_Price = Bidder_1
            else:
                Final_Price = Bidder_2

            print(last_Bidder, "Bidded for ", Final_Price)

        for m in range(1, 5):
            if player_info[m][5] == last_Bidder:
                player_info[m][3] = player_info[m][3] - Final_Price
                player_info[m][2].append(property)
                print("The property has been added to your profile and the money has been deducted")
                print(player_info[m][1], "'s balance is", player_info[m][3])
                for n in range(0, 40):
                    if n == property:
                        board_info[n][11] = player_info[m][1]

    elif bidders == 3:
        player_1 = keys[0]
        player_2 = keys[1]
        player_3 = keys[2]
        bidders_1 = Bidders_Dict[player_1]
        bidders_2 = Bidders_Dict[player_2]
        bidders_3 = Bidders_Dict[player_3]
        property = x
        print("Auction is for", property)
        last_Bidder = 'To Solve Error'  # Will take the bidder 1 and 2 index wise
        Final_Price = 0
        prop_number = 0
        for x in range(1, 41):
            if board_info[x][0] == property:
                prop_number = x
        Base_price = board_info[prop_number][2]
        Bidder_1, Bidder_2, Bidder_3 = 0, 0, 0
        flag, c = 0, 0
        Bid = ''
        print(Bidders_Dict[player_1][1], "should write", Bidders_Dict[player_1][5], 'to bid and ',
              Bidders_Dict[player_2][1], " should write ", Bidders_Dict[player_2][5], "To Bid and ",
              Bidders_Dict[player_3][1], "Should write ", Bidders_Dict[player_3][5])
        print("Press 'Enter' to stop bidding")
        while True:
            Bid = input("Enter initial to bid")
            if Bid != Bidders_Dict[player_1][5] and Bid != Bidders_Dict[player_2][5] and Bid != '' and Bid != \
                    Bidders_Dict[player_3][5]:
                print("Enter Valid input")
                continue
            if Bid == last_Bidder:
                print("You can't bid on yourself")
                continue  # Checked if same person didn't rebid
            c += 1  # Won't Add when Wrong bid is placed
            Current_Bid = int(Base_price) + 5 * c
            if Bid == Bidders_Dict[player_1][5]:
                if Bidders_Dict[player_1][3] > Current_Bid:
                    Bidder_1 = Current_Bid
                    # Current_Bid = int(Base_price) + 5 * c
                else:
                    print("You don't have enough funds")
                    Current_Bid = Current_Bid - 5
                    Final_Price=Current_Bid
                    if Bidder_3 > Bidder_2:
                        l_Bidder = player_3
                    else:
                        l_Bidder = player_2
                    last_Bidder = Bidders_Dict[l_Bidder][5]
                    print("Property goes to", last_Bidder, "for", Final_Price)
                    break
            if Bid == Bidders_Dict[player_2][5]:
                if Bidders_Dict[player_2][3] > Current_Bid:
                    Bidder_2 = Current_Bid
                else:
                    print("You don't have enough funds")
                    Current_Bid = Current_Bid - 5
                    Final_Price=Current_Bid
                    if Bidder_1 >= Bidder_3:
                        l_Bidder = player_1
                    else:
                        l_Bidder = player_3
                    last_Bidder = Bidders_Dict[l_Bidder][5]
                    print("Property goes to", last_Bidder, "for", Final_Price)
                    break
            if Bid == Bidders_Dict[player_3][5]:
                if Bidders_Dict[player_2][3] > Current_Bid:
                    Bidder_1 = Current_Bid  # theek karje
                    # Current_Bid = int(Base_price) + 5 * c
                else:
                    print("You don't have enough funds")
                    Current_Bid = Current_Bid - 5
                    Final_Price = Current_Bid
                    if Bidder_1 > Bidder_2:
                        l_Bidder = player_1
                    else:
                        l_Bidder = player_2
                    last_Bidder = Bidders_Dict[l_Bidder][5]
                    print("Property goes to", last_Bidder, "for", Final_Price)
                    break
            if Bid == '':
                print("Property goes to", last_Bidder, "for", Final_Price)
                break

            if Bid == Bidders_Dict[player_1][5] or Bid == Bidders_Dict[player_2][5] or Bid == Bidders_Dict[player_3][5]:
                last_Bidder = Bid

            if Bidder_1 > Bidder_2:
                if Bidder_3 < Bidder_1:
                    Final_Price = Bidder_1

            elif Bidder_1 < Bidder_2:
                if Bidder_3 < Bidder_2:
                    Final_Price = Bidder_2

            elif Bidder_1 < Bidder_3:
                if Bidder_3 > Bidder_1:
                    Final_Price = Bidder_3

            print(last_Bidder, "Bidded for ", Final_Price)
        if bidders != 1:
            for m in range(1, 5):
                if player_info[m][5] == last_Bidder:
                    player_info[m][3] = int(player_info[m][3]) - int(Final_Price)
                    player_info[m][2].append(property)
                    print("The property has been added to your profile and the money has been deducted")
                    print(player_info[m][1], "'s balance is", player_info[m][3])
                    for n in range(0, 40):
                        if n == property:
                            board_info[n][11] = player_info[m][1]


def prop(position):
    if board_info[position][11] == '':
        print("You landed at", board_info[position][0])
        print("The price is ", board_info[position][1])
        print("Your Bank Balance is", player_info[player][3])
        while True:
            ask_1 = input("Do you want to buy it (y/n) ?").lower()
            # place belongs to 1)no one 2)some other one 3)himself/herself
            if ask_1 == 'y':
                if player_info[player][3] <= 0:
                    print("Insufficient Funds")
                    break
                else:
                    # change bank balance,add property in his list,add his name in the property dict
                    board_info[position][4] += 1
                    player_info[player][3] = player_info[player][3] - board_info[position][1]
                    board_info[position][11] = player_info[player][1]
                    player_info[player][2].append(board_info[position][0])
                    print("Congrats on purchase")

                break
            elif ask_1 == 'n':
                print("Thank you for visiting, have a great stay.")
                break
            else:
                print('Enter valid input')

    elif board_info[position][11] != player_info[player][1] and board_info[position][11] != '':
        # name,print rent,rent_deduct,rent_add,balance,bankrupt
        print("Your current balance is", player_info[player][3])
        print("You landed on", board_info[position][0])
        print("Property owner is", board_info[position][11])
        print("The rent is", board_info[position][3])

        if int(player_info[player][3]) >= int((board_info[position][4]) * int(board_info[position][3])):
            player_info[player][3] = player_info[player][3] - (board_info[position][4] * board_info[position][3])
            for j in players:  # changed i to player to avoid out of index error
                if player_info[j][1] == board_info[position][11]:
                    owner = j
                    player_info[owner][3] = player_info[owner][3] + (board_info[position][4] * board_info[position][3])
        else:
            print("You are bankrupted")
            print("You are now removed from the game.")
            print("Thank You for playing")
            players.remove(player)
            rem_property = player_info[player][2]
            for k in rem_property:
                print("Commencing the Auction")
                bidding(k)


    elif board_info[position][11] == player_info[player][1]:
        # build more (max 5),continue
        print("You landed on ", board_info[position][0])
        print("Your balance is this ", player_info[player][3])
        print("Price per house is ", board_info[position][2])
        ask_2 = input("Do you want to build more (y/n) ?").lower()
        if ask_2 == 'y':
            # balance conditions
            if player_info[player][3] > player_info[player][3]:
                if board_info[position][4] < 5:
                    board_info[position][4] += 1
                    player_info[player][3] = player_info[player][3] - player_info[player][3]
                else:
                    print("Maximum level reached")
            else:
                print("Cannot proceed due to insufficient funds")
                print()


        else:
            print("Thanks for visiting")


def comm_chance(temp_Dice):
    print(Chance_Cards[temp_Dice][0])
    player_info[player][3] = player_info[player][3] + Chance_Cards[temp_Dice][1]
    if player_info[player][3] <= 0:
        print("You are bankrupted")
        print("You are now removed from the game.")
        print("Thank You for playing")
        players.remove(player)
        rem_property = player_info[player][2]
        for k in rem_property:
            print("Commencing the Auction")
            bidding(k)


def tax():
    print("Oh..No!!!......Pay ₹200 Income Tax ")
    player_info[player][3] = player_info[player][3] - 200
    if player_info[player][3] <= 0:
        print("You are bankrupted")
        print("You are now removed from the game.")
        print("Thank You for playing")
        players.remove(player)
        rem_property = player_info[player][2]
        print(player_info[player])
        for k in rem_property:
            bidding(k)


def parking():
    print("Landed on free parking......")
    print("Please have some tea while you wait !!")


def go():
    player_info[player][3] = player_info[player][3] + 200
    print("You just passed GO.")
    print("You received ₹200")


board_info = {40: ['Boardwalk', 400, 200, 50, 0, 600, 1400, 1700, 2000, 200, 'Prop', ''],
              39: ['Income Tax', 0, 0, 200, 0, 0, 0, 0, 0, 0, 'Tax', ''],
              38: ['Park Place', 350, 200, 35, 0, 500, 1100, 1300, 1500, 175, 'Prop', ''],
              37: ['Chance', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Chance', ''],
              36: ['Short Line', 200, 100, 16, 0, 220, 600, 800, 1000, 100, 'Prop', ''],
              35: ['Pennsylvania Avenue', 320, 200, 28, 0, 450, 1000, 1200, 1400, 160, 'Prop', ''],
              34: ['Community Chest', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Com_Chest', ''],
              33: ['North Carolina Avenue', 300, 200, 26, 0, 390, 900, 1100, 1275, 150, 'Prop', ''],
              32: ['Pacific Avenue', 300, 200, 26, 0, 390, 900, 1100, 1275, 150, 'Prop', ''],
              31: ['Go to Jail', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'ToJail', ''],
              30: ['Marvin Gardens', 280, 150, 24, 0, 360, 850, 1025, 1200, 140, 'Prop', ''],
              29: ['Water Works', 160, 100, 12, 0, 180, 500, 700, 900, 80, 'Prop', ''],
              28: ['Ventnor Avenue', 260, 150, 22, 0, 330, 800, 975, 1150, 130, 'Prop', ''],
              27: ['Atlantic Avenue', 260, 150, 22, 0, 330, 800, 975, 1150, 130, 'Prop', ''],
              26: ['B. & O. Railroad', 200, 100, 16, 0, 220, 600, 800, 1000, 100, 'Prop', ''],
              25: ['Illinois Avenue', 240, 150, 20, 0, 300, 750, 925, 1100, 120, 'Prop', ''],
              24: ['Indiana Avenue', 220, 150, 18, 0, 250, 700, 875, 1050, 110, 'Prop', ''],
              23: ['Chance', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Chance', ''],
              22: ['Kentucky Avenue', 220, 150, 18, 0, 250, 700, 875, 1050, 110, 'Prop', ''],
              21: ['Free Parking ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Parking', ''],
              20: ['New York Avenue', 200, 100, 16, 0, 220, 600, 800, 1000, 100, 'Prop', ''],
              19: ['Tennessee Avenue', 180, 100, 14, 0, 200, 550, 750, 950, 90, 'Prop', ''],
              18: ['Community Chest', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Com_Chest', ''],
              17: ['St. James Place', 180, 100, 14, 0, 200, 550, 750, 950, 90, 'Prop', ''],
              16: ['Pennsylvania Railroad', 200, 100, 16, 0, 220, 600, 800, 1000, 100, 'Prop', ''],
              15: ['Virginia Avenue', 160, 100, 12, 0, 180, 500, 700, 900, 80, 'Prop', ''],
              14: ['States Avenue', 140, 100, 10, 0, 150, 450, 625, 750, 70, 'Prop', ''],
              13: ['Electric Company', 160, 100, 12, 0, 180, 500, 700, 900, 80, 'Prop', ''],
              12: ['St. Charles Place', 140, 100, 10, 0, 150, 450, 625, 750, 70, 'Prop', ''],
              11: ['Jail', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'ToJail', ''],
              10: ['Connecticut Avenue', 120, 50, 8, 0, 100, 300, 450, 600, 60, 'Prop', ''],
              9: ['Vermont Avenue', 100, 50, 6, 0, 90, 270, 400, 550, 50, 'Prop', ''],
              8: ['Chance', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Chance', ''],
              7: ['Oriental Avenue', 100, 50, 6, 0, 90, 270, 400, 550, 50, 'Prop', ''],
              6: ['Reading Railroad', 200, 100, 16, 0, 220, 600, 800, 1000, 100, 'Prop', ''],
              5: ['Income Tax', 0, 0, 200, 0, 0, 0, 0, 0, 0, 'Tax', ''],
              4: ['Baltic Avenue', 60, 50, 4, 0, 60, 180, 320, 450, 30, 'Prop', ''],
              3: ['Community Chest', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Com_Chest', ''],
              2: ['Mediterranean Avenue', 60, 50, 2, 0, 30, 90, 160, 250, 30, 'Prop', ''],
              1: ['Go', 0, 0, 200, 0, 0, 0, 0, 0, 0, 'Go', '']}

# {number: [position,name,properties,balance,property_money,player_token]
player_info = {1: [1, "name", [], 1000, "property_money", "car"],
               2: [1, "name", [], 1000, "property_money", "bike"],
               3: [1, "name", [], 1000, "property_money", "boat"],
               4: [1, "name", [], 1000, "property_money", "dog"]}

Chance_Cards = {1: ["Advance to Go (Collect $200)", 200],
                2: ["Bank error in your favor. Collect $200", 200],
                3: ["Doctor’s fee. Pay $50", -50],
                4: ["From sale of stock you get $50", 50],
                5: ["Holiday fund matures. Receive $100", 100],
                6: ["Income tax refund. Collect $20", 20],
                7: ["Pay hospital fees of $100", -100],
                8: ["Pay school fees of $50", -50],
                9: ["Receive $25 consultancy fee", 25],
                10: ["You have won second prize in a beauty contest. Collect $10", 10],
                11: ["You inherit $100", 100],
                12: ["Go to Jail: Go directly to jail, do not pass Go, do not collect $200", 'jail', -200,
                     "(To counter for crossing the start)"]}
Reconstruct = 0
players = []
Didnt_play = 0
player_tokens = ["car", "bike", "boat", "dog"]
print("1.New Game,2.Continue ")
Q0 = int(input("Enter Number:"))

if Q0 == 2:
    Didnt_play = 1
    players = []
    print("Fetching data")
    for i in [1, 2, 3, 4]:  # Check if there is any data in the file,And then reconstructing dictionary for the players
        if i == 1:
            try:
                f1 = open("Player_1_info.txt", 'r')
                line_1 = f1.readline()
                f1.close()
                if line_1 != '':
                    players.append(i)
                    Reconstruct = 1
            except FileNotFoundError:
                f1 = open("Player_1_info.txt", 'w')
                f1.close()

        if i == 2:
            try:
                f1 = open("Player_2_info.txt", 'r')
                line_1 = f1.readline()
                f1.close()
                if line_1 != '':
                    players.append(i)
                    Reconstruct = 1
            except FileNotFoundError:
                f1 = open("Player_2_info.txt", 'w')
                f1.close()
        if i == 3:
            try:
                f1 = open("Player_3_info.txt", 'r')
                line_1 = f1.readline()
                f1.close()
                if line_1 != '':
                    players.append(i)
                    Reconstruct = 1
            except FileNotFoundError:
                f1 = open("Player_3_info.txt", 'w')
                f1.close()

        if i == 4:
            try:
                f1 = open("Player_4_info.txt", 'r')
                line_1 = f1.readline()
                f1.close()
                if line_1 != '':
                    players.append(i)
                    Reconstruct = 1
            except FileNotFoundError:
                f1 = open("Player_4_info.txt", 'w')
                f1.close()
        if players == []:
            print("You Don't have a saved game...")
            Didnt_play = 0
            Reconstruct = 0
            break

if Q0 == 1 or Didnt_play == 0:
    Q1 = int(input("Enter Number of players(2,3,4)"))
    for i in range(0, Q1):
        print("player_", i + 1)
        print("player tokens", player_tokens)
        while True:
            Q2 = input("Select one token (Exactly copy player token)").lower().strip()
            if Q2 == "car":
                player_tokens.remove(Q2)
                Q2 = 1
                break
            elif Q2 == "bike":
                player_tokens.remove(Q2)
                Q2 = 2
                break
            elif Q2 == "boat":
                player_tokens.remove(Q2)
                Q2 = 3
                break
            elif Q2 == "dog":
                player_tokens.remove(Q2)
                Q2 = 4
                break
            else:
                print("enter valid input")
        Q3 = input("Enter a name")
        player_info[Q2][1] = Q3
    print("Setting up the Board")
    f1 = open('Player_1_info.txt', 'w')
    a = ""
    f1.write(a)
    f1.close()
    f1 = open('Player_2_info.txt', 'w')
    a = ""
    f1.write(a)
    f1.close()
    f1 = open('Player_3_info.txt', 'w')
    a = ""
    f1.write(a)
    f1.close()
    f1 = open('Player_4_info.txt', 'w')
    a = ""
    f1.write(a)
    f1.close()
# Time
for i in range(5, -1, -1):
    'time.sleep(5)'
    print('\r', i, end='')
    time.sleep(1)
print()

if Reconstruct == 0:
    players = []
    for i in [1, 2, 3, 4]:
        if player_info[i][1] != "name":
            players.append(i)
elif Reconstruct == 1:
    for i in players:
        if i == 1:
            f1 = open("Player_1_info.txt", 'r')
            l1 = []
            a = 0
            while True:
                line_1 = f1.readline()
                l1.append(line_1)
                a += 1
                if a == 6:
                    break
            player_info[1][0] = int(l1[0])
            player_info[1][1] = l1[1].strip('\n')
            # player_info[1][2] = list(l1[2])
            player_info[1][3] = int(l1[3])
            q = 0
            l_4 = l1[4].strip('\n').split(',')  # To avoid using list
            l_4 = l_4[1:]
            l_5 = l1[5].split(',')
            l_5 = l_5[1:]
            for p in l_4:
                board_info[int(p)][11] = player_info[i][0]
                board_info[int(p)][4] = l_5[q]
                q += 1
            property_have_list = []
            for q in l_4:
                temp = board_info[int(q)][0]
                property_have_list.append(temp)
            player_info[1][2].extend(property_have_list)
            f1.close()
            l_4.clear()
            l_5.clear()
        if i == 2:
            f1 = open("Player_2_info.txt", 'r')
            l2 = []
            a = 0
            while True:
                line_1 = f1.readline()
                l2.append(line_1)
                a += 1
                if a == 6:
                    break
            player_info[2][0] = int(l2[0])
            player_info[2][1] = l2[1].strip('\n')
            # player_info[2][2] = list(l2[2]) #theek karje
            player_info[2][3] = int(l2[3])
            q = 0

            l_4 = l2[4].strip('\n').split(',')  # To avoid using list
            l_4 = l_4[1:]
            l_5 = l2[5].split(',')
            l_5 = l_5[1:]
            for p in l_4:
                board_info[int(p)][11] = player_info[i][0]
                board_info[int(p)][4] = l_5[q]
                q += 1
            property_have_list_1 = []
            for q in l_4:
                temp = board_info[int(q)][0]
                property_have_list_1.append(temp)
            player_info[2][2].extend(property_have_list_1)
            f1.close()
            l_4.clear()
            l_5.clear()
        if i == 3:
            f1 = open("Player_3_info.txt", 'r')
            l3 = []
            a = 0
            while True:
                line_1 = f1.readline()
                l3.append(line_1)
                a += 1
                if a == 6:
                    break
            player_info[3][0] = int(l3[0])
            player_info[3][1] = l3[1].strip('\n')
            # player_info[3][2] = list(l3[2])
            player_info[3][3] = int(l3[3])
            q = 0
            l_4 = l3[4].strip('\n').split(',')  # To avoid using list
            l_4 = l_4[1:]
            l_5 = l3[5].split(',')
            l_5 = l_5[1:]
            for p in l_4:
                board_info[int(p)][11] = player_info[i][0]
                board_info[int(p)][4] = l_5[q]
                q += 1
            property_have_list_3 = []
            for q in l_4:
                temp = board_info[int(q)][0]
                property_have_list_3.append(temp)
            player_info[3][2].extend(property_have_list_3)
            f1.close()
            l_4.clear()
            l_5.clear()
        if i == 4:
            f1 = open("Player_4_info.txt", 'r')
            l4 = []
            a = 0
            while True:
                line_1 = f1.readline()
                l4.append(line_1)
                a += 1
                if a == 6:
                    break
            player_info[4][0] = int(l4[0])
            player_info[4][1] = l4[1].strip('\n')
            player_info[4][2] = list(l4[2])
            player_info[4][3] = int(l4[3])
            q = 0
            l_4 = l4[4].strip('\n').split(',')  # To avoid using list
            l_4 = l_4[1:]
            l_5 = l4[5].split(',')
            l_5 = l_5[1:]
            for p in l_4:
                board_info[int(p)][11] = player_info[i][0]
                board_info[int(p)][4] = l_5[q]
                q += 1
            property_have_list_4 = []
            for q in l_4:
                temp = board_info[int(q)][0]
                property_have_list_4.append(temp)
            player_info[4][2].extend(property_have_list_4)
            f1.close()
            l_4.clear()
            l_5.clear()

# main body
Flag_of_rounds = 0
Go_Counter = 0
jail_counter = 0
Initial_player = players
while True:  # will run loops after everyone's turn
    if Flag_of_rounds == 1:
        if Initial_player != players:  # If someone goes bankrupt then the main list will be updated after a round so
            Initial_player = players  # no ones turn is skipped
        for k in players:
            if k == 1:  # Rewrites every single time so updated data
                f1 = open("Player_1_info.txt", 'w')
                property_board_info = player_info[k][2]
                property_board_info_len = len(property_board_info)
                property_list_1 = ""
                property_list_lvl_1 = ""
                for o in range(0, property_board_info_len):  # property dictionary keys
                    pos = player_info[k][2][o]
                    for r in range(1, 41):
                        if pos == board_info[r][0]:
                            property_list_1 = property_list_1 + "," + str(r)
                            property_list_lvl_1 = property_list_lvl_1 + "," + str(board_info[r][4])
                data = str(player_info[k][0]) + '\n' + str(player_info[k][1]) + '\n' + str(
                    player_info[k][2]) + '\n' + str(
                    player_info[k][3]) + '\n' + str(property_list_1) + '\n' + str(property_list_lvl_1)
                f1.write(data)
                f1.close()
            if k == 2:
                f2 = open("Player_2_info.txt", 'w')
                property_board_info = player_info[k][2]
                property_board_info_len = len(property_board_info)
                property_list_2 = ""
                property_list_lvl_2 = ""
                for o in range(0, property_board_info_len):  # property dictionary keys
                    pos = player_info[k][2][o]
                    for r in range(1, 41):
                        if pos == board_info[r][0]:
                            property_list_2 = property_list_2 + "," + str(r)
                            property_list_lvl_2 = property_list_lvl_2 + "," + str(board_info[r][4])
                data = str(player_info[k][0]) + '\n' + str(player_info[k][1]) + '\n' + str(
                    player_info[k][2]) + '\n' + str(
                    player_info[k][3]) + '\n' + str(property_list_2) + '\n' + str(property_list_lvl_2)
                f2.write(data)
                f2.close()
            if k == 3:
                f3 = open("Player_3_info.txt", 'w')
                property_board_info = player_info[k][2]
                property_board_info_len = len(property_board_info)
                property_list_3 = ""
                property_list_lvl_3 = ""
                for o in range(0, property_board_info_len):  # property dictionary keys
                    pos = player_info[k][2][o]
                    for r in range(1, 41):
                        if pos == board_info[r][0]:
                            property_list_3 = property_list_3 + "," + str(r)
                            property_list_lvl_3 = property_list_lvl_3 + "," + str(board_info[r][4])
                data = str(player_info[k][0]) + '\n' + str(player_info[k][1]) + '\n' + str(
                    player_info[k][2]) + '\n' + str(
                    player_info[k][3]) + '\n' + str(property_list_3) + '\n' + str(property_list_lvl_3)
                f3.write(data)
                f3.close()
            if k == 4:
                f4 = open("Player_4_info.txt", 'w')
                property_board_info = player_info[k][2]
                property_board_info_len = len(property_board_info)
                property_list_4 = ""
                property_list_lvl_4 = ""
                for o in range(0, property_board_info_len):  # property dictionary keys
                    pos = player_info[k][2][o]
                    for r in range(1, 41):
                        if pos == board_info[r][0]:
                            property_list_4 = property_list_4 + "," + str(r)
                            property_list_lvl_4 = property_list_lvl_4 + "," + str(board_info[r][4])
                data = str(player_info[k][0]) + '\n' + str(player_info[k][1]) + '\n' + str(
                    player_info[k][2]) + '\n' + str(
                    player_info[k][3]) + '\n' + str(property_list_4) + '\n' + str(property_list_lvl_4)
                f4.write(data)
                f4.close()
        print("moves are auto saved....!")
        ask_quit = input("Do you want to Pause?(y/n)").lower()
        if ask_quit == 'y':
            print("Your progress is saved and you can continue later")
            break
    for i in Initial_player:  # position
        Flag_of_rounds = 1
        time.sleep(2)
        print()
        player = i
        Current_player_info = player_info[i]
        position = player_info[i][0]
        print(Current_player_info[1], "'s turn")  # When first player is having his first move the position wont
        # update but if car is given to the second player this error doesnt occur
        print(player_info[i][5], "'s position is:", position)
        if (position == 11 and jail_counter == 0) or (position == 31 and jail_counter == 0):
            jail_counter = 1
            print("player", i, "is in jail")
            print()
        else:
            while True :
                Ask_p=input("""Press Enter to Roll the dice and p to see your progress""")
                if Ask_p=='':
                    break
                else:
                    print("Name:", player_info[i][1])
                    print("Position:",player_info[i][0])
                    print("Balance:",player_info[i][3])
                    print("Properties:",player_info[i][2])

            temp_Dice = int(input("Enter the roll output"))  # dice_double()ADD AFTER TESTING
            print("You rolled", temp_Dice)
            time.sleep(1)  # Time for player to interpret
            position = position + temp_Dice
            if position > 40:
                position = position - 40
                go()
                Go_Counter = 1

            print("New Position:", position)
            player_info[i][0] = position

            if board_info[position][10] == 'Go':
                if Go_Counter != 1:
                    go()
                    Go_Counter = 0

                print("Your Balance:", Current_player_info[3])
                continue
            elif board_info[position][10] == 'Prop':
                prop(position)

                print("Your Balance:", Current_player_info[3])
                continue
            elif board_info[position][10] == 'Com_Chest':
                print("You landed on Community Chest.")
                comm_chance(temp_Dice)

                print("Your Balance:", Current_player_info[3])
                continue
            elif board_info[position][10] == 'Chance':
                print("You landed on Chance.")
                comm_chance(temp_Dice)

                print("Your Balance:", Current_player_info[3])
                continue
            elif board_info[position][10] == 'Parking':
                parking()
                print("Your Balance:", Current_player_info[3])
                continue
            elif board_info[position][10] == 'Tax':
                tax()

                print("Your Balance:", Current_player_info[3])
                continue
            elif board_info[position][10] == 'ToJail':
                print("You landed in jail")
            print()
