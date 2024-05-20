from Vehicle import Vehicle
from Customer import Customer

class RentalManagement(Vehicle, Customer):

    def print():
        print("Hi")



if __name__ == '__main__':
    rent = RentalManagement()