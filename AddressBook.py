"""
@Author:Vijay Kumar M N
@Date: 2024-09-12
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-09-12
@Title : python program for the AddressBook to add the contacts.
"""

class contact:
    def __init__(self,First_Name,Last_Name,Address,City,State,Zip_Code,Phone_Number,Email):
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Address=Address
        self.City=City
        self.State=State
        self.Zip_Code=Zip_Code
        self.Phone_Number=Phone_Number
        self.Email=Email
    def display_Contacts(self):
        return (f"Name: {self.First_Name} {self.Last_Name}\n"
                f"Address: {self.Address}, {self.City}, {self.State}, {self.Zip_Code}\n"
                f"Phone: {self.Phone_Number}\n"
                f"Email: {self.Email}\n")
class AddressBook:
    def __init__(self):
        self.contacts={}
    
    def add_contact(self,contact):
        
        """
        Description:
            This method is used to add a contact to the address book.
             If the contact already exists, it will print a message.
        
        Parameters:
            contact (Contact): The contact object to be added.
        
        Returns:
            None
        
        """
       
        key=f"{contact.First_Name} {contact.Last_Name}"
        if key not in self.contacts:
            self.contacts[key]=contact
        else:
            print("Contact already exists")
    def display_all_contacts(self):
        if not self.contacts:
            print("\nNo contacts found in the Address Book.\n")
        else:
            print("\nAll Contacts:\n")
            for contact in self.contacts.values():
                print(contact.display_Contacts())
                

def main():
    
    """
    Description:
        This function is used to display the welcome message.

    Parameters:
        None
    
    Returns:
        None
    """
    print("-----------------------Welcome to Address Book--------------------")

    address_book=AddressBook()
    
    while True:
        print("------ADDRESS BOOK MENU-------")
        print('\n 1. Add new Contact:')
        print("\n 2. Display contacts")

        choice=int(input("Enter the choice:"))
        if choice==1:    
            First_Name=input("Enter the First Name:")
            Last_Name=input("Enter the Last Name:")
            Address=input("Enter the Address:")
            City=input("Enter the City:")
            State=input("Enter the State:")
            Zip_Code=input("Enter the Zip Code:")
            Phone_Number=int(input("Enter the Phone Number:"))
            Email=input("Enter the Email:")
    
            contacts=contact(
                First_Name=First_Name,
                Last_Name=Last_Name,
                Address=Address,
                City=City,
                State=State,
                Zip_Code=Zip_Code,
                Phone_Number=Phone_Number,
                Email=Email
            )
            address_book.add_contact(contacts)
        elif choice==2:
            address_book.display_all_contacts()
        else:
            break

if __name__=="__main__":
    main()