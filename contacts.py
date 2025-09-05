"""
TASK: Create a ContactBook class.

Requirements:
1. Store contacts in a dictionary (name → phone number).
2. Provide a method to add new contacts.
3. Provide a method to delete contacts.
4. Provide a method to search for a contact by name.
5. Provide a method to show all contacts.

Example Usage:
    book = ContactBook()
    book.add_contact("Alice", "08012345678")
    print(book.search_contact("Alice"))  # "08012345678"
"""
class ContactBook:
    def __init__(self):
        self.contacts=[]
    def add_contact(self,name,phone_no):
        self.contacts.append({name:phone_no})
    def delete_contact(self, name):
        for contact in self.contacts:
            if name in contact:
                self.contacts.remove(contact)
            else:
                continue
    def search_contact(self,name):
        for contact in self.contacts:
            if name in contact:
                return contact[name]
    def show_contacts(self):
        return self.contacts
    

book = ContactBook()
print(book.show_contacts())
book.add_contact("Alice", "08012345678")
print(book.search_contact("Alice"))
print(book.show_contacts())