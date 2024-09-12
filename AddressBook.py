"""
@Author:Vijay Kumar M N
@Date: 2024-09-11
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-09-11
@Title : python program for the AddressBook.
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

  
if __name__=="__main__":
    main()