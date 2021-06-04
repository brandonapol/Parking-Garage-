# Your parking gargage class should have the following methods:
class Parking_garage():

    '''
        The program should take the following input types:
        - tickets should be lists
        - spaces should be a list
        - current_ticket is a dictionary
    '''

    def __init__(self, tickets = [], spaces = [], current_ticket = {}):
        self.tickets = tickets
        self.spaces = spaces 
        self.current_ticket = current_ticket

    def decision_tree(self):
        while True:
            result = input('Would you like a ticket? y/n ')
            if result.lower() == 'y':
                Parking_garage.take_ticket(self)
            elif result.lower() == 'n':
                break
            else:
                print('That is not a valid answer')

# - takeTicket
    def take_ticket(self):
        if len(self.spaces) == 0:
            print("We're full! Sorry")
        else:
            new_ticket = self.tickets.pop(0)
            new_space = self.spaces.pop(0)
            self.current_ticket[new_ticket] = "unpaid"
            print(self.spaces)
    
    
        

# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking


    def pay_for_parking(self):
        pass

# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True


# -leaveGarage

    def leave_garage(self):
        pass
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

def run_garage():
    ticket_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    spaces_available = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    garage = Parking_garage(ticket_list, spaces_available)
    garage.decision_tree()

run_garage()   
