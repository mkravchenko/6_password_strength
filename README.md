# 6_password_strength

1. Download any file with most used passwords:<br />
    https://github.com/danielmiessler/SecLists/tree/master/Passwords<br />
2. Run the program:<br />
    python password_strength.py<br />
3. Enter the path to the file that you download on step 1.<br />
4. Enter your password.<br />
5. To exit push "Enter" button.<br />

# Examples of usage:<br />

Enter the password: 93<br />
The password strength is: 1

Enter the password: ^&*<br />
The password strength is: 1

Enter the password: asdfdas<br />
The password strength is: 2

Enter the password: fadas!@#<br />
The password strength is: 6

Enter the password: asdfasdf*)&$%*$&#$$%*&^)*(&)(&*)_&*<br />
The password strength is: 8

Enter the password: sdafsdufpisduafu-e8w7tr7348703289JOUGOpafhu<br />
The password strength is: 9

Enter the password: asdfsdiafudsa$%+)_(*)hlsdfjhda69786597HHHI<br />
The password strength is: 10
