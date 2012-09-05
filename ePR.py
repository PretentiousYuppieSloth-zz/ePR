'''
Created on 24/08/2012
@author: litek
'''
#!/usr/bin/env python
#
#TODO:
#Implement mailbox.Maildir if possible. 
#http://docs.python.org/library/mailbox.html
#

#imports listed here.
    #Email.message is used so i can call the email.message_from_string() parsing function 
    #email.utils is used so i can call the get_all() function to extract FROM and TO fields from the Email
import email

    #allow regular expressions (for email extration process)
import re

    #include OS so we can list files in our directory
import os

    #allow usage of sqlite
import sqlite3

print "Welcome to ePigeon Raper 0.1"
print "ePR is a rather simple data extraction utility developed with"
print "the purpose of mapping major email leaks. Feel free to hack it"
print "muck it up and so on. It is just a \"learn to python\" project"
print "\nImporting mail.\n"


    #Global vars  SE SAA AT FAA KOMMENTEREDE DINE VARIABLER !!! KETIL
mailcounter = 0
folder_size = 0
numlines = 0
mailfile = ""
filepath = ""
conn = ""
cur = ""
walkpath = ""
top_level_dir = "."



    #Functions
def openfiles():
    try :
        #take filename from file in our foreachloop and open via filehandle and stream into var mailfile
        fileHandle = open( filepath, 'r' )
        global mailfile
        mailfile = fileHandle.read()
        fileHandle.close()
    except IOError as e:
        #handle possible filename errors
        print "\tImport error: " + str(e) + "\n"
        print "Application closed"
        exit()
def dataextraction():
    global  mailcounter
    global  numlines
    global  filepath
    global  folder_size
    global  path
    global  lines
    
    
    for file_loop in os.listdir(path):
        slash = "/"
        filepath = path + slash + file_loop
        if os.path.isfile(filepath):
            openfiles() #call openfiles function
            #enumerate amount of lines in file
            for lines in open(filepath): 
                numlines += 1
                 
                #Parse imported file to a format get_all() can handle
            msg = email.message_from_string(mailfile)
                #if file checked returns None(no email addresses), skip to next file(loop)
            if msg.get('To') is None:
                continue 
            
            #get current filesize and put it into filesize var, append current filesize to folder_size to count amount of data
            filesize = os.path.getsize(filepath)
            folder_size += filesize
            
                #Get wanted fields via msg.get(), use regular expressions to remove unnessasarry gunk,stuff and poop, then print results.        
            TO_str = re.findall(r"([\w\-\._0-9]+@[\w\-\._0-9]+)",  str(msg.get('To')), re.UNICODE)[0]        
            FROM_str = re.findall(r"([\w\-\._0-9]+@[\w\-\._0-9]+)", str(msg.get('from')), re.UNICODE)[0]
            #print "\tTO: " + str(TO_str) + "\tFROM: " + str(FROM_str) +"\tFileSize = %0.7f MB" % (filesize/(1024*1024.0)) +"\tPath:" + str(filepath)
            
            
            cur.execute("INSERT INTO Pidgeon_Nest VALUES ('"+ TO_str +"','"+FROM_str+"','"+str(filepath)+"') ")
            #conn.commit()
            #register filepath for the individual file, for later database logging
            filepath = os.path.abspath(filepath)
            #count each file processed amount of loops (files handled)
            mailcounter += 1



def Sqlconnection():
    global conn
    global cur
    conn = sqlite3.connect("PigeonLoft.db")
    cur = conn.cursor()
def SqlCreateTable():
    cur.execute("CREATE TABLE IF NOT EXISTS Pidgeon_Nest (m_from, m_to, m_filename)")
    conn.commit()

def processDirectory ( args, dirname, filenames ):
    global path                            
    path = dirname
    dataextraction()



Sqlconnection()
SqlCreateTable()

os.path.walk(top_level_dir, processDirectory, None)


print "\nFinished!\n"    + "\t  Files processed:" + str(mailcounter) +"\t\tData processed:%0.2fMB" % (folder_size/(1024*1024.0)) + "\t\tNumber of Lines:" + str(numlines)  +"\n"