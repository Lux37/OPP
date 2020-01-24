class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.2
        return pounds

    def weight_to_inch(self):
        pounds = self.height_cm / 2.54
        return inches

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name,last_name,height_cm,weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name,last_name,height_cm,weight_kg)
        self.point = points
        self.rebounds = rebounds
        self.assists = assists

ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=678,
                         yellow_cards=95, red_cards=11)
kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=204, weight_kg=95, points=104,
                         rebounds=152, assists=36)

print(ronaldo.first_name)
print(ronaldo.last_name)
print(ronaldo.goals)
print(ronaldo.weight_kg)
print(ronaldo.weight_to_lbs())
print(ronaldo.first_name + ", " + ronaldo.last_name)
print(ronaldo.first_name + "\n" + ronaldo.last_name)

print(kev_dur.first_name)
print(kev_dur.last_name)
print(kev_dur.weight_kg)

