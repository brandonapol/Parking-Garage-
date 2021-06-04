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
            result = input('How can we help? \n - Get Ticket ("Get") \n - Checkout ("Checkout") \n - Quit ("Quit")\n - Help ("Help")')
            if result.lower() == 'get':
                Parking_garage.take_ticket(self)
            elif result.lower() == 'checkout':
                Parking_garage.pay_for_parking(self)
                print("Have a great day! Watch for moose!")
                break
            elif result.lower() == 'quit':
                break
            else:
                print('''\n\nPlease type one of the following prompts: \nFor recieving a ticket and gaining access to the garage, \nplease type "Get".\nFor checking out and escaping the parking garage,\nplease type "Checkout". \nIf you'd like to quit the process and not get a ticket, type "Quit".\n\n\n''')

# - takeTicket
    def take_ticket(self):
        if len(self.spaces) == 0:
            print("We're full! Sorry")
        else:
            new_ticket = self.tickets.pop(0)
            new_space = self.spaces.pop(0)
            print(f'Your ticket number is {new_ticket}')
            self.current_ticket[new_ticket] = "unpaid"
            print(self.spaces)
 

# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking


    def pay_for_parking(self):
        for key, value in self.current_ticket.items():
            if value == 'unpaid':
                response = input("Would you like to checkout? y/n ")
                if response.lower() == 'y':
                    print(self.current_ticket)
                    ticket_key = input('What was your ticket number?')
                    ticket_key_update = int(ticket_key)
                    self.current_ticket[ticket_key_update] = 'paid'
                    print(self.current_ticket)
                    ticket_number_temp = self.current_ticket.pop(key)
                    self.spaces.append(ticket_key_update)
                    print(sorted(self.spaces))
                    # printed_number
                    # need to add space back
                    print("Thanks for your money. You have 15 minutes to leave.")
                    # self.spaces.insert(len(self.spaces) + 1)
                    Parking_garage.decision_tree()
                elif response.lower() == 'n':
                    Parking_garage.decision_tree()
            else:
                print('You have already paid. Get out')



# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True


# -leaveGarage

 #   def leave_garage(self):
  #      pass
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
