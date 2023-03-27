# Email-Simulator
This program is a simple email simulator that allows users to send, receive, read, mark as spam, and delete emails.

# Installation

To use this program, Python must be installed on your system. 
You can download and install the latest version of Python from the official website: https://www.python.org/downloads/

# How to use this program

Clone this repository to your local machine. Navigate to the program's directory.

<br>

Simply run the program:
```
email.py
```
<br>

Once the program is running, you will be prompted with a list of actions you can perform:
```
s  -  send email
l  -  list emails from a sender
r  -  read email
m  -  mark email as spam
gu -  get unread emails
gs -  get spam emails
d  -  delete email
e  -  exit program
```

Follow the prompts to perform the desired action.

~~~
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[INBOX]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

1: ✉  From: dreams@sky.net    Subject: DREAMS
2: ✉  From: dreams@sky.net    Subject: HOPE
3: ✉  From: sky@dreams.net    Subject: TRUTH
4: ✉  From: kofi@coffee.cc    Subject: COFFEE
5: ✉  From: tea@teatime.tt    Subject: TEA

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

Welcome to the email system! What would you like to do?

s  -  send email.
l  -  list emails from a sender.
r  -  read email.
m  -  mark email as spam.
gu -  get unread emails.
gs -  get spam emails.
d  -  delete email.
e  -  exit this program.
l
Please enter the address of the sender
:dreams@sky.net
════════════════ ✉  from » dreams@sky.net « ═════════════════

1: DREAMS
2: HOPE


▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[INBOX]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

1: ✉  From: dreams@sky.net    Subject: DREAMS
2: ✉  From: dreams@sky.net    Subject: HOPE
3: ✉  From: sky@dreams.net    Subject: TRUTH
4: ✉  From: kofi@coffee.cc    Subject: COFFEE
5: ✉  From: tea@teatime.tt    Subject: TEA

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

Welcome to the email system! What would you like to do?

s  -  send email.
l  -  list emails from a sender.
r  -  read email.
m  -  mark email as spam.
gu -  get unread emails.
gs -  get spam emails.
d  -  delete email.
e  -  exit this program.
r
Please enter the address of the sender of the email
:dreams@sky.net
════════════════ Read ✉  from » dreams@sky.net « ═════════════════

1: DREAMS
2: HOPE

Please enter the index of the email that you would like to read
:1
════════════════ Read ✉  » Subject DREAMS « ═════════════════

Contents: Follow your dreams

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[INBOX]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

1: ✉  From: dreams@sky.net    Subject: DREAMS
2: ✉  From: dreams@sky.net    Subject: HOPE
3: ✉  From: sky@dreams.net    Subject: TRUTH
4: ✉  From: kofi@coffee.cc    Subject: COFFEE
5: ✉  From: tea@teatime.tt    Subject: TEA

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

Welcome to the email system! What would you like to do?

s  -  send email.
l  -  list emails from a sender.
r  -  read email.
m  -  mark email as spam.
gu -  get unread emails.
gs -  get spam emails.
d  -  delete email.
e  -  exit this program.
e
Goodbye
~~~  


![alt text](https://github.com/filosoho/Email-Simulator/blob/deae57df6c55dee5f6f3d7956f7f818f366da070/Email%20Simulator.jpg?raw=true)

![alt text](https://github.com/filosoho/Email-Simulator/blob/cf22b6e15eec2413330e7b66dbb76b25f6fcba58/Email%20Simulator-1.png?raw=true)


# Contributing

If you have any suggestions or find any bugs, please feel free to open an issue or submit a pull request.
