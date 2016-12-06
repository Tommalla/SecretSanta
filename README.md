# SecretSanta
A simple script for secret santa lotteries supporting lottery emails

Usage:
``python santa.py names.txt template.txt``

names.txt:  
A list of names (one name per line) to conduct the lottery on. The
format is:
``First_name Rest_of_the_name email@email.sth.whatever``

template.txt:  
The template for the message that will be sent. The two supported
tags are ``<PERSON_FIRSTNAME>`` - first name of the person giving
the present and ``TARGET_NAME`` - full name of the receiver.  
You can write whatever you want in the template. The script will
only subsititute the tags.
