# Project name: Check Profanity
# Course: Udacity Full Stack Nanodegree

# -----------------------------------

import urllib2
   
def read_text():
    quotes = open("/Users/Alexander/Documents/Coding/0_Portfolio/Udacity_Full_Stack_Developer/01_Programming_with_Python/Lesson 5/sample_email.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib2.urlopen('http://www.wdylike.appspot.com/?q='+urllib2.quote(text_to_check))
    output = connection.read()
    connection.close()

    if "true" in output:
        print ("Profanity Alert!")
    elif "false" in output:
        print ("This document has no curse words!")
    else:
        print ("Could not scan the document properly.")
    
read_text()
