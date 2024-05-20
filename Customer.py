

class Customer:

    def __init__(self, name: str, contact_details: int, driving_license: str) -> None:
        self.name = name
        self.contact_details = contact_details
        self.driving_license = driving_license

    def get_customer_info(self):
        return {"Name: "+self.name+" Contact Details: "+str(self.contact_details)+" Driving License: "+self.driving_license}
    

if __name__ == '__main__':
    customer = Customer("Geddam Siva Prasad Reddy", 9640718354, "AP23AJ890")
    print(customer.get_customer_info())