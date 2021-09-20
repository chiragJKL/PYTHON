class TRAIN:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("\n******************************\n")
        print(f"Seats available {self.seats}.")
        print(
            f"Your Train is {self.name}. Please pay rs. {self.fare}/- kindely.")
        # print("\n******************************\n")

    def getSeats(self):
        # print("\n******************************\n")
        self.seats = self.seats - 1
        print(f"Your ticket conformed!! Now seats left {self.seats}.")
        print("\n******************************\n")

    def cancel(self):
        cancel = int(
            input("ENTER 1 for CANCELLATION or ENTER 2 to complete the process : "))

        if cancel == 1:
            self.seats = self.seats + 1
            print(
                f"Cancellation successful! Now tickets available {self.seats}")
        else:
            print("thank you for choosing IRCTC")


train1 = TRAIN("Rajdhani Ex", 89, 250)
train1.getStatus()
train1.getSeats()
train1.cancel()
