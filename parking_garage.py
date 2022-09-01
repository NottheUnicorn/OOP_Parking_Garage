from cProfile import run


class parking_garage:
    
    """
       Your parking garage class should have the following methods:
- takeTicket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1
- payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

    """
    
    def __init__(self):
        self.tickets = 50
        self.parking_spaces = 50
        self.current_ticket = {}
        
    # Method that decreases the parking spaces by 1 and the number of tickets by 1
    def take_ticket(self):
            self.tickets -= 1
            self.parking_spaces -= 1
    
    # method to recieve payment and increase parking spaces in lot
    def pay_for_parking(self):
        self.payment = input("Can I please have your payment of 10 dollars?: ")
        if self.payment != "":
            print("Your ticket has been paid and you have 15 mins to leave!")
            self.parking_spaces += 1
            self.current_ticket['paid'] = True
        
    # establishing a car leaving the garage and the ticket total and parking spaces increasing by 1 
    def leave_garage(self):
        while self.payment == "":
            self.payment = input("Please pay for parking!")
        print("Thank you, Have a nice day!")
        self.tickets += 1
        self.parking_spaces += 1 
            
          
garage = parking_garage()
garage.take_ticket()
garage.pay_for_parking()
garage.leave_garage()
