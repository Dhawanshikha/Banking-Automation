# Banking-Automation
Banking Automation system is a windows based applications. This project mainly deals with managing accounts and their related operations.

Python script for a simple banking automation system using Tkinter for GUI and SQLite for database management. It includes functionalities like user login, creating 
new accounts, depositing and withdrawing funds, transferring funds between accounts, viewing transaction history, and updating user profiles.

### Import Necessary Modules: 
The script imports required modules such as Tkinter for GUI, SQLite for database operations, and datetime for handling date and time.
### Create Database Tables: 
The script attempts to create two tables in an SQLite database named "Banking.sqlite" if they don't already exist. One table stores account information, and the other stores transaction history.
### Define GUI Screens and Functions:
Main Screen:  This screen allows users to sign in, create a new account, or reset the form.

New User Screen: Users can register for a new account on this screen.

Forget Password Screen: Users can retrieve their password by providing account details.

Login Screen: After successful login, users can access various banking functionalities like viewing account details, updating profile, depositing, withdrawing, transferring funds, and viewing transaction history.
### Main Loop: 
The win.mainloop() function starts the GUI application, ensuring it stays responsive to user interactions.
