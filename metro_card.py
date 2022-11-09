class MetroCard:
    tickets_available = 30
    locations = {'london': 2, 'peterborough': 4, 'manchester': 6}
    card_fee = 1

    def __init__(self):
        pass

    def __repr__(self):
        return "This machine has {tickets} available".format(tickets=self.tickets_available)

    def print_locations():
        tickets = MetroCard.locations
        for key, value in tickets.items():
            print(f"{key}: £{value}")