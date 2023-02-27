# This program is an email simulator.

# Create a class definition for an 'Email'.
class Email:
    '''This is a simple email model.'''
    
    def __init__(self, from_address, subject_line, email_contents):
        '''The initializer takes in three arguments and stores them as instance-level variables 
        (from_address, subject_line, email_contents). In addition, the initializer will create 
        two more instance-level variables (has_been_read, is_spam) with default False values.
        '''
        
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False
    
    def mark_as_read(self):
        '''Mark an email as read.'''
        
        self.has_been_read = True

    def mark_as_spam(self):
        '''Mark an email as spam.'''
        
        self.is_spam = True

    def __str__(self):
        '''Returns a neatly formatted descriptive name.'''
        
        return f"From: {self.from_address}    Subject: {self.subject_line}" # Read: {self.has_been_read} Spam: {self.is_spam} Contents: {self.email_contents}"


# Create a class definition for an 'Inbox'.
class Inbox:
    '''This is a simple model to simulate an inbox.'''

    def __init__(self):
        '''The initializer doesn’t take any arguments, and only initializes an empty list. 
        This list is where all of Email objects will be stored
        '''
        
        self.emails = []

    def __str__(self):
        '''Returns a neatly formatted descriptive name 
        (an email object with it's index number incremented by 1)
        '''
        
        messages = [
            f"{i + 1}: ✉  {email} "
            for i, email in enumerate(self.emails)
            ]
        return "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[INBOX]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n" + "\n".join(messages) + "\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"

    def add_email(self, from_address, subject_line, email_contents):
        '''Takes in the contents and email address from the received
        email to make a new Email object and store it in the inbox
        '''
        
        email = Email(from_address, subject_line, email_contents)
        self.emails.append(email)
        return email

    def list_messages_from_sender(self, sender_address):
        '''Returns a string showing all subject lines in emails from a specific sender, 
        along with a corresponding number. 
        ''' 
        
        # Initialise a variable 'messages' list. 
        # We want to get an email that has 'sender_address' and we want its subject line with a corresponding index number incremented by 1.
        # To do that, iterate through all email objects using enumerate.
        # Then check if the email address in the email object is the same as the 'sender_address'.       
        messages = [
            f"{i + 1}: {email.subject_line}"
            for i, email in enumerate(self.emails)
            if email.from_address == sender_address            
        ]
        # Check if the length of the 'messages' is equal to 0.
        if len(messages) == 0:
            return "\nNo messages from this sender."            
        else:
            # Return a string of 'messages' joined by '\n'.
            return  "\n" + "\n".join(messages) + "\n"

    def get_email(self, sender_address, email_index):
        '''Returns the email at a specific index from a specific user or indicates that nothing was found.'''

        # Check if 'email_index' is equal or greater than 0 and if 'email_index' is less 
        # than the length of the 'emails' list of objects.
        if email_index >= 0 and email_index < len(self.emails):
            # Initialise 'email_found' to an email object and its index.
            email_found = self.emails[email_index]
            # Check if the email address of 'email_found' does not equal to 'sender_address'.
            if email_found.from_address != sender_address:
                # Set 'email_found' to None.
                email_found = None
            return email_found

    def mark_as_spam(self, sender_address, email_index):
        '''Marks the email at a specific index within a sender address as spam.'''
        
        # Initialise a variable 'email_found' to a method 'get_email' with arguments 'sender_address, email_index'.
        email_found = self.get_email(sender_address, email_index)
        # Check if 'email_found' is not None.
        if email_found is not None:
            # Use 'mark_as_spam' method on the 'email_found' object.
            email_found.mark_as_spam()
        return email_found

    def get_unread_emails(self):
        '''Returns a string containing a list of all the emails that haven’t been read. 
        Only the subject lines need to be shown
        '''
        
        # Initialise a variable 'unread_emails' with a list.
        # We want to get only the subject line from the email object.
        # Iterate through email object in 'emails' list.
        # Check if the email has been read. 
        unread_emails = [
            email.subject_line
            for email in self.emails
            if not email.has_been_read
        ]        
        if unread_emails:
            # Return a string of subject line from the email joined by '\n'.
            return "\n" + "\n".join(unread_emails) + "\n"
        else:
            return "\nNo unread emails found."

    def get_spam_emails(self):
        '''Returns a string containing a list of all the emails that have been marked as spam.'''
        
        # Initialise a variable 'spam_emails'.
        # We want to get an index of the email, its address and subject.
        # Iterate through all the email objects in the 'emails' list.
        # Check if the email is a spam.
        spam_emails = [f"{i + 1}: ✉  From: {email.from_address}    Subject: {email.subject_line}"
            for i, email in enumerate(self.emails) if email.is_spam
            ]        
        if spam_emails:
            # Return a string of index, email address and subject line from the email joined by '\n'.
            return "\n" + "\n".join(spam_emails) + "\n"
        else:
            return "\nNo spam emails found."   

    def delete_email(self, sender_address, email_index):
        '''Deletes an email at a specific index within a sender address in the inbox.'''

        # Initialise a variable 'email_found' to a method 'get_email' with arguments 'sender_address, email_index'.
        email_found = self.get_email(sender_address, email_index)
        # Check if 'email_found' is not None.
        if email_found is not None:
            # Delete 'email_found' object from the 'emails' list.
            self.emails.remove(email_found)
        return email_found     


# Create a new instance of the class 'Inbox()' and assign this object to a variable 'inbox'.
inbox = Inbox()


#--------------------------------------- Additional comments -------------------------
# This is an additional help to test the program. It will add example emails to the 'emails' list.
# It is an example of an Inbox with 5 emails.
# If you do not wish to use this, please comment this section out.
#-----------------------------Comment out-------------------------------
inbox.add_email("dreams@sky.net", "DREAMS", "Follow your dreams")
inbox.add_email("dreams@sky.net", "HOPE", "Believe in yourself")
inbox.add_email("sky@dreams.net", "TRUTH", "Keep seeking the truth")
inbox.add_email("kofi@coffee.cc", "COFFEE", "Drink a cup of coffee")
inbox.add_email("tea@teatime.tt", "TEA", "Drink a cup of tea")
#-----------------------------Comment out-------------------------------


# Initialise a variable 'usage_message' to display a menu with options.
usage_message = '''
Welcome to the email system! What would you like to do?

s  -  send email.
l  -  list emails from a sender.
r  -  read email.
m  -  mark email as spam.
gu -  get unread emails.
gs -  get spam emails.
d  -  delete email.
e  -  exit this program.
'''
# Initialise a variable 'user_choice' with an empty string.
user_choice = ""
while True:

    #-------------------- Additional comment -------------- ----------------
    # This will print out the example email Inbox with 5 example emails.
    # If you do not want to use it, please comment it out.
    #-----------------------------Comment out-------------------------------
    print(inbox)
    #-----------------------------Comment out-------------------------------

    # Ask the user to choose an option from the 'usage_message' menu, 
    # strip it and format to a lowercase. 
    user_choice = input(usage_message).strip().lower()

    if user_choice == "s":
        # Send an email (Create a new Email object)
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        contents = input("Please enter the contents of the email\n:")

        # Now add the email to the Inbox
        inbox.add_email(sender_address, subject_line, contents)

        # Print a success message
        print("\nEmail has been added to inbox.")
    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")
        print(f"════════════════ ✉  from » {sender_address} « ═════════════════")        
        # Now list all emails from this sender
        print(inbox.list_messages_from_sender(sender_address))
    elif user_choice == "r":
        # Read an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        print(f"════════════════ Read ✉  from » {sender_address} « ═════════════════")
        # Now list all emails from this sender
        messages_from_sender = inbox.list_messages_from_sender(sender_address)
        print(messages_from_sender)

        # Check if 'messages_from_sender' is not '\nNo messages from this sender.'
        if messages_from_sender != "\nNo messages from this sender.":
            # Initialise a variable 'indx' to False.
            indx = False            
            while indx == False:
                try:
                    # Step 3: ask the user for the index of the email
                    email_index = int(input("Please enter the index of the email that you would like to read\n:")) - 1

                    # Step 4: display the email
                    email = inbox.get_email(sender_address, email_index)

                    # Check if the 'email' is not None.
                    if email != None:
                        print(f"════════════════ Read ✉  » Subject {email.subject_line} « ═════════════════")
                        print("\nContents:", email.email_contents)
                        # Mark the email as read.
                        email.mark_as_read()
                        # Set a variable 'indx' to True.
                        indx = True
                    else:
                        print("ERROR.Incorrect email index number. Try again.\n")
                except (ValueError):
                    print("Incorrect input. Try again\n")
        else:
            continue
    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        
        # Step 2: show all emails from this sender (with indexes)
        print(f"══════════════ SPAM ✉  from » {sender_address} « ═══════════════")        
        # Now list all emails from this sender
        messages_from_sender = inbox.list_messages_from_sender(sender_address)
        print(messages_from_sender)

        # Check if 'messages_from_sender' is not '\nNo messages from this sender.'
        if messages_from_sender != "\nNo messages from this sender.":
            # Initialise a variable 'indx' to False.
            indx = False            
            while indx == False:
                try:
                    # Step 3: ask the user for the index of the email
                    email_index = int(input("Please enter the index of the email to be marked as spam\n:")) - 1
                    # Step 4: mark the email as spam
                    email = inbox.mark_as_spam(sender_address, email_index)
                    # Step 5: print a success message
                    if email is not None:
                        print(f"═════════ ✉  from » {sender_address} « Subject: {email.subject_line} ════════")       
                        print("\nEmail has been marked as spam.")
                        indx = True
                    else:
                        print("ERROR.Incorrect email index number. Try again.\n")
                except (ValueError):
                    print("Incorrect input. Try again\n")
        else:
            continue
    elif user_choice == "gu":
        # List all unread emails
        unread_emails = inbox.get_unread_emails()
        print(f"═════════════════════════ Unread ✉  ══════════════════════════")
        print(unread_emails)
    elif user_choice == "gs":
        # List all spam emails
        spam_emails = inbox.get_spam_emails()
        print(f"══════════════════════════ Spam ✉  ═══════════════════════════")
        print(spam_emails)
    elif user_choice == "e":
        # Quit the program.
        print("Goodbye")
        break
    elif user_choice == "d":
        # Delete an email.
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        print(f"═════════════ Delete ✉  from » {sender_address} « ═════════════")
        # Step 2: show all emails from this sender (with indexes)
        messages_from_sender = inbox.list_messages_from_sender(sender_address)
        print(messages_from_sender)

        # Check if 'messages_from_sender' is not '\nNo messages from this sender.'
        if messages_from_sender != "\nNo messages from this sender.":
            # Initialise a variable 'indx' to False.
            indx = False
            while indx == False:
                try:
                    # Step 3: ask the user for the index of the email
                    email_index = int(input("Please enter the index of the email to be deleted\n:")) - 1
                    # Step 4: delete the email
                    email = inbox.delete_email(sender_address, email_index)
                    # Step 5: print a success message
                    if email is not None: 
                        print(f"══════ Delete ✉  from » {sender_address} « Subject: {email.subject_line} ══════")      
                        print("\nEmail deleted.")
                        indx = True
                    else:
                        print("ERROR.Incorrect email index number. Try again.\n")
                except ValueError:
                    print("Incorrect input. Try again\n")
        else:
            continue
    else:
        # Invalid choice.
        print("\nOops - incorrect input")


