"""
@Author:Vijay Kumar M N
@Date: 2024-09-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-09-13
@Title : Python program for to sort the contacts in the address book based on the city or state.
"""

import re
from MyLogging import logger_init

class contact:
    def __init__(self, First_Name, Last_Name, Address, City, State, Zip_Code, Phone_Number, Email):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Address = Address
        self.City = City
        self.State = State
        self.Zip_Code = Zip_Code
        self.Phone_Number = Phone_Number
        self.Email = Email

    def display_Contacts(self):
        """
        Description:
            This function returns the contact details as a string.
        
        Parameters:
            None
        
        Returns:
            str: Contact details as a string.
        """
        return (f"Name: {self.First_Name} {self.Last_Name}\n"
                f"Address: {self.Address}, {self.City}, {self.State}, {self.Zip_Code}\n"
                f"Phone: {self.Phone_Number}\n"
                f"Email: {self.Email}\n")

    def update_contact(self, Address=None, City=None, State=None, Zip_Code=None, Phone_Number=None, Email=None):
        """
        Description:
            This function updates the contact's details if new values are provided.
        
        Parameters:
            Address: str Updated address.
            City : str Updated city.
            State : str Updated state.
            Zip_Code : str Updated zip code.
            Phone_Number: str Updated phone number.
            Email: str Updated email.
        
        Returns:
            None
        """
        
        if Address:
            self.Address = Address
        if City:
            self.City = City
        if State:
            self.State = State
        if Zip_Code:
            self.Zip_Code = Zip_Code
        if Phone_Number:
            self.Phone_Number = Phone_Number
        if Email:
            self.Email = Email

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    class AddressBook:
        def __init__(self):
            self.contacts = {}

        def add_contact(self, contact):
           
            """
             Description:
                This method is used to add a contact to the address book.
                If the contact already exists, it will print a message.
        
            Parameters:
                contact (Contact): The contact object to be added.
        
            Returns:
                None
            """
            key = f"{contact.First_Name} {contact.Last_Name}"
            if key not in self.contacts:
                self.contacts[key] = contact
                print("Contact added successfully.")
                logger_init("UC_11").info(f"Contact added successfully: {key}")
            else:
                print("Contact already exists.")
                logger_init("UC_11").info(f"Contact already exists: {key}")
            
        
        
        def edit_contact(self, first_name, last_name):
            
            """
            Description:
                This function allows editing an existing contact's details.
        
            Parameters:
                first_name : str First name of the contact to edit.
                last_name : str Last name of the contact to edit.
        
            Returns:
                str: Success or failure message.
            """
            
            key = f"{first_name} {last_name}"
            if key in self.contacts:
                print("Leave blank to retain the current value.")
                Address = input("Enter new Address (or press Enter to skip): ")
                City = input("Enter new City (or press Enter to skip): ")
                State = input("Enter new State (or press Enter to skip): ")
                Zip_Code = AddressBookSystem.get_valid_zip_code(input("Enter new Zip Code (or press Enter to skip): "))
                Phone_Number = AddressBookSystem.get_valid_phone_number(input("Enter new Phone Number (or press Enter to skip): "))
                Email = AddressBookSystem.get_valid_email(input("Enter new Email (or press Enter to skip): "))

                self.contacts[key].update_contact(
                    Address=Address if Address else None,
                    City=City if City else None,
                    State=State if State else None,
                    Zip_Code=Zip_Code if Zip_Code else None,
                    Phone_Number=Phone_Number if Phone_Number else None,
                    Email=Email if Email else None
                )
                logger_init("UC_11").info(f"Contact edited successfully: {key}")
                return f"Contact {key} edited successfully."
            else:
                logger_init("UC_11").info(f"Contact {key} not found.")
                return f"Contact for {key} not found."

        
        def delete_contact(self, first_name, last_name):
            """
            Description:
                This function is used to delete the contact based on the first name and last name.

            Parameters:
                First_Name : str First name of the contact to delete.
                Last_Name : str Last name of the contact to delete
        
            Returns:
                str:
            """
            key = f"{first_name} {last_name}"
            if key in self.contacts:
                del self.contacts[key]
                logger_init("UC_11").info(f"Contact deleted successfully: {key}")
                return f"Contact deleted successfully."
            else:
                logger_init("UC_11").info(f"Contact {key} not found.")
                return f"Contact does not exist."
        
        
        def sort_by_name(self):
            """
            Description:
                This function is used to sort the names 
            
            Parameters:
                None
            
            Returns:
                result """
            sorted_contacts = sorted(self.contacts.values(), key=lambda x: (x.First_Name, x.Last_Name))
            result = "\nSorted Contacts:\n"
            for contact in sorted_contacts:
                result += contact.display_Contacts()
                print("\n")
            return result
        
        def sort_by_city_state(self,name):
            """
            Description:
                This function used to sort based on the city or state.
                
            Parameters:
                name: str its city or state
            
            returns:
                 result"""
            if name=='state':
                sorted_contacts = sorted(self.contacts.values(), key=lambda x: x.State)
                result = "\nSorted by State:\n"
                for contact in sorted_contacts:
                    result += contact.display_Contacts()
                    result += "\n"
                return result
            else:
                sorted_contacts = sorted(self.contacts.values(), key=lambda x: x.City)
                result = "\nSorted by City:\n"
                for contact in sorted_contacts:
                    result += contact.display_Contacts()
                    result += "\n"
                return result

        
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
                return "\nNo contacts found in the Address Book.\n"
            else:
                result = "\n All Contacts:\n"
                for contact in self.contacts.values():
                    result += contact.display_Contacts()
                return result

    def create_address_book(self, name):
        """
        Description:
            Creates a new address book with a unique name.
        
        Parameters:
            name: str Address Book Name
        
        Returns:
            str
        
        """
        if name not in self.address_books:
            self.address_books[name] = self.AddressBook()
            logger_init("UC_11").info(f"Address Book '{name}' created successfully.")
            return f"Address Book '{name}' created successfully."
            
        else:
            logger_init("UC_11").info(f"Address Book '{name}' already exists.")
            return f"Address Book '{name}' already exists."
            

    def get_address_book(self, name):
        """
        Description:
            Returns the address book with the given name.
        
        Parameters:
            name:str Address Book name
        
        Returns:
            str
        
        """
        if name  in self.address_books:
            return self.address_books.get(name)
            
        else:
            
            return  None
    def search_city_state(self,city=None,state=None):

        """
        Description:
            This function is used to search a person by city or state.
            
        Parameters:
            city:Nonee
            state:None
        
        Returns:
            result: str"""
        count=0
        result="\n SEARCH RESULTS \n"
        for book_name,address_book in self.address_books.items():
            for contact in address_book.contacts.values():
                if (city and contact.City==city) or (state and contact.State==state):
                    result += f"Address Book: {book_name}\n" + contact.display_Contacts()
                    count+=1
        return result if result != "\nSearch Results:\n" else "No matching contacts found.",count

            
    @staticmethod
    def get_valid_zip_code(zip_code_input):
        """
        Description:
            This function ensures that the entered Zip Code is valid (6 digits).
        
        Parameters:
            zip_code_input: str The input Zip Code.
        
        Returns:
            str: A valid 6-digit Zip Code.
        """
        attempts = 1
        while not re.match(r"^\d{6}$", zip_code_input) and attempts <= 3:
            print("Invalid Zip Code. Please enter a 6-digit number.")
            zip_code_input = input("Enter a valid Zip Code: ")
            attempts += 1
        return zip_code_input

    
    
    @staticmethod
    def get_valid_email(email_input):
        """
         Description:
            This function ensures that the entered Email is valid.
        
        Parameters:
            Email_input: str The input Email.
        
        Returns:
            str: A valid Email.
        """
        attempts = 1
        while not re.match(r"^[\w]+([._+#$%^&*-][\w]+)*@[\w]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$", email_input) and attempts <= 3:
            print("Invalid Email. Please enter a valid email (e.g., vijaykumar@gmail.com).")
            email_input = input("Enter a valid Email: ")
            attempts += 1
        return email_input

    
    
    @staticmethod
    def get_valid_phone_number(phone_number_input):
        """
         Description:
            This function ensures that the entered valid phone number.
        
        Parameters:
            Phone_Number_input: str The input phone number.
        
        Returns:
            str: A valid 10 digits phone number.
        """
        attempts = 1
        while not re.match(r"\d{10}", phone_number_input) and attempts <= 3:
            print("Invalid phone number. Please enter a valid 10-digit number.")
            phone_number_input = input("Enter a valid Phone Number: ")
            attempts += 1
        return phone_number_input


def main():
    
    print("----------------------- Welcome to the Address Book --------------------")
    system = AddressBookSystem()

    while True:
        print("\n------ ADDRESS BOOK SYSTEM MENU -------\n")
        print("1. Create new Address Book")
        print("2. Select Address Book")
        print("3.Search a person by state or city")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the Address Book name: ")
            result=system.create_address_book(name)
            print(result)

        elif choice == 2:
            name = input("Enter the Address Book name: ")
            address_book = system.get_address_book(name)
            if address_book:
                while True:
                    print(f"\n---- {name} Address Book Menu ----")
                    print("1. Add new Contact")
                    print("2. Display Contacts")
                    print("3. Edit Contact")
                    print("4. Delete Contact")
                    print("5. Sort by Name")
                    print("6. Sort By City or State")
                    print("7. Go Back")

                    sub_choice = int(input("Enter your choice: "))
                    if sub_choice == 1:
                        First_Name = input("Enter the First Name: ")
                        Last_Name = input("Enter the Last Name: ")
                        Address = input("Enter the Address: ")
                        City = input("Enter the City: ")
                        State = input("Enter the State: ")
                        Zip_Code = AddressBookSystem.get_valid_zip_code(input("Enter the Zip Code: "))
                        Phone_Number = AddressBookSystem.get_valid_phone_number(input("Enter the Phone Number: "))
                        Email = AddressBookSystem.get_valid_email(input("Enter the Email: "))

                        contact_obj = contact(First_Name, Last_Name, Address, City, State, Zip_Code, Phone_Number, Email)
                        address_book.add_contact(contact_obj)

                    elif sub_choice == 2:
                        print(address_book.display_all_contacts())

                    elif sub_choice == 3:
                        First_Name = input("Enter the First Name: ")
                        Last_Name = input("Enter the Last Name: ")
                        print(address_book.edit_contact(First_Name, Last_Name))

                    elif sub_choice == 4:
                        First_Name = input("Enter the First Name: ")
                        Last_Name = input("Enter the Last Name: ")
                        print(address_book.delete_contact(First_Name, Last_Name))
                    
                    elif sub_choice==5:
                        result=address_book.sort_by_name()
                        print(result)
                    
                    elif sub_choice==6:
                        result=input("Enter how to sort based on city or state")
                        print(address_book.sort_by_city_state(result))

                    elif sub_choice == 7:
                        break

                    else:
                        print("Invalid choice, please try again.")

            else:
                print(f"No Address Book found with the name '{name}'.")
        elif choice==3:
            City=input("Enter the city to search ( or press enter to skip)")
            State=input("Enter the state to search ( or press enter to skip)")
            if City or State:
                result,count=system.search_city_state(City,State)
                print(result)
                print(f"The Number of Persons found is: {count}")

                logger_init("UC_11").info("Search found ")
            else:
                print("There are no persons on that particular city or state.")
                logger_init("UC_11").info("Search not found ")

        elif choice == 4:
            print("Exiting the Address Book System.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()