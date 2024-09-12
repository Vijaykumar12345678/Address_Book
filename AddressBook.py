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
    contacts=contact()
    address_book.add_contact(contacts)
  
if __name__=="__main__":
    main()