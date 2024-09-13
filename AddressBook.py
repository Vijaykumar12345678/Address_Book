"""
@Author:Vijay Kumar M N
@Date: 2024-09-12
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-09-12
@Title : python program for the AddressBook to add the contacts.
"""
import re
from MyLogging import logger_init
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
        """
        Description:
            This function is used to print the contacts
            
        Parameters:
            None

        Returns:
            str: all the contacts
            """
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
        
        self.contacts[key]=contact
        print("Contact Added Successfully")
        logger_init("UC_2").info(f"Contact Added  Successfully:")

    def get_valid_zip_code(self, zip_code_input):
        
        """
        Description:
            This function ensures that the entered Zip Code is valid (6 digits).
        
        Parameters:
            zip_code_input: str The input Zip Code.
        
        Returns:
            str: A valid 6-digit Zip Code.
        """
        
        attempts=1
        while not re.match(r"^\d{6}$", zip_code_input) and attempts<=3:
            print("Invalid Zip Code. Please enter a 6-digit number.")
            zip_code_input = input("Enter a valid Zip Code: ")
            attempts+=1
        return zip_code_input
    
    def get_valid_Email(self, Email_input):
    
        """
        Description:
            This function ensures that the entered Email is valid.
        
        Parameters:
            Email_input: str The input Email.
        
        Returns:
            str: A valid Email.
        """
        attempts=1
        while not re.match(r"^[\w]+([._+#$%^&*-][\w]+)*@[\w]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$", Email_input) and attempts<=3:
            print("Invalid Email. Please enter a valid mail (ex:vijaykumar@gmail.com).")
            Email_input = input("Enter a valid Email: ")
            attempts+=1
        return Email_input 

    def get_valid_Phone_Number(self, Phone_Number_input):
        """
        Description:
            This function ensures that the entered valid phone number.
        
        Parameters:
            Phone_Number_input: str The input phone number.
        
        Returns:
            str: A valid 10 digits phone number.
        """
        attempts=1
        while not re.match(r"\d{10}", Phone_Number_input) and attempts<=3:
            print("Invalid Email. Please enter a valid phone number (eg:8861912898).")
            Phone_Number_input = input("Enter a valid Phone Number: ")
            attempts+=1
        return Phone_Number_input    
    
    
    
    def display_all_contacts(self):

        """
        Description:
            This function is used to display all the contacts.
        
        Parameters:
            None
        
        Returns:
            result: str 
        """
        
        if not self.contacts:
            result="\nNo contacts found in the Address Book.\n"
        else:
            result="\n All Contacts:\n"
            for contact in self.contacts.values():
                result+=contact.display_Contacts()
            return result

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
        print("\n------ADDRESS BOOK MENU-------\n")
        print('\n 1. Add new Contact:')
        print("\n 2. Display contacts")

        choice=int(input("Enter the choice:"))
        if choice==1:    
            First_Name=input("Enter the First Name:")
            Last_Name=input("Enter the Last Name:")
            Address=input("Enter the Address:")
            City=input("Enter the City:")
            State=input("Enter the State:")
            Zip_Code=address_book.get_valid_zip_code(input("Enter the Zip Code:"))
            Phone_Number=address_book.get_valid_Phone_Number((input("Enter the Phone Number:")))
            Email=address_book.get_valid_Email(input("Enter the Email:"))
    
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
            result=address_book.display_all_contacts()
            print(result)
        else:
            break

if __name__=="__main__":
    main()