'''
Created on 24/08/2012
@author: litek
'''
#!/usr/bin/env python


#imports listed here. #Email.message is used so i can call the email.message_from_string() parsing function     #email.utils is used so i can call the get_all() function to extract FROM and TO fields from the Email
import email

    #allow regular expressions (for email extration process)
import re

    #include OS so we can list files in our directory
import os

    #allow usage of sqlite
import sqlite3

    #Lets generate them hashes after sorting the TO and FROM field.
import hashlib

    # cPickle is imported to do serialization data for the MD5 hash.
import cPickle as pickle


print "Welcome to ePigeon Raper 0.1"
print "ePR is a rather simple data extraction utility developed with"
print "the purpose of mapping major email leaks. Feel free to hack it"
print "muck it up and so on. It is just a \"learn to python\" project"
print "\nImporting mail.\n"


#GO Through your frekking variables and figure out which ones need to be local and which need to be global


    #Global vars  Comment your frekking Variables    
mailcounter = 0                 #Count the amounts of mails 
folder_size = 0                 #Calculate folder size
numlines = 0                    #Calculate number of lines processed
mailfile = ""                   #???
filepath = ""                   #???
conn = ""                       #sqlite connection 
cur = ""                        #????
walkpath = ""                   #????
top_level_dir = "emails"     #Directory to perform data extraction on.
data_md5 = ""                   #MD5_Hash
UniqIdent = ""                  #for the concatenated ID-String
TO_str = ""                     #
FROM_str = ""                   #
unique_ID_dict = {}             # Dictionary for sql appended mail lookup

mailuniqueid_dict = {}          #so we can check whether or not we have registered the ID already
mailuniqueid_counter_TO = 0     #Iterative count for the TO_mails
mailuniqueid_counter_FROM = 0   #Iterative count for the FROM mails
mailunique_count = 0
FROM_ID = 0
TO_ID = 0


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

def Sort_append():
    global FROM_str
    global TO_str
    global UniqIdent
    global data_md5
    global unique_ID_dict
    if FROM_str < TO_str:
        UniqIdent = FROM_str + "__" + TO_str
        data = [UniqIdent]
        data_pickle = pickle.dumps(data)
        data_md5 = hashlib.md5(data_pickle).hexdigest()

    else:
        #concatenate strings for ID-String
        UniqIdent = TO_str + "__" + FROM_str
        #Generate MD5 Hash for the MD5-Hash.
        data = [UniqIdent]
        data_pickle = pickle.dumps(data)
        data_md5 = hashlib.md5(data_pickle).hexdigest()

def uniqueID_gen():
    global mailuniqueid_counter_TO
    global mailuniqueid_counter_FROM
    global mailunique_count
    global mailuniqueid_dict
    global FROM_ID
    global TO_ID
    
    
    if mailuniqueid_dict.has_key(FROM_str):
        FROM_ID = str(mailuniqueid_dict[FROM_str])
    else:
        mailunique_count += 1
        mailuniqueid_dict[FROM_str] = mailunique_count
        FROM_ID = str(mailuniqueid_dict[FROM_str])
        
    if mailuniqueid_dict.has_key(TO_str): 
        TO_ID = str(mailuniqueid_dict[TO_str])
    else:
        mailunique_count += 1
        mailuniqueid_dict[TO_str] = mailunique_count
        TO_ID = str(mailuniqueid_dict[TO_str])
    
def dataextraction():
    global  mailcounter
    global  numlines
    global  filepath
    global  folder_size
    global  path
    global  lines
    global data_md5
    global UniqIdent
    global TO_str
    global FROM_str
    global mailuniqueid_counter_TO
    global mailuniqueid_counter_FROM
    global mailunique_count
    global mailuniqueid_dict
    global FROM_ID
    global TO_ID
    
    Message_ID = ""             #GET the Message-ID from the email
    
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
            
            #make everything lowercase so the md5_hash wount be different even though its the same email
            TO_str = TO_str.lower()
            FROM_str = FROM_str.lower()
            
            #Generate unique ID's for each email address
            uniqueID_gen()
            '''
            Just here to debug the unique id generator if needed
            print "FROM_ID: " + str(mailuniqueid_dict[FROM_str]) + "\t" + FROM_str
            print "TO_ID: " + TO_ID + "\t" + TO_str +"\n"
            '''
            
            #GET the Message-ID from the email (this should later be used to analyze if we have double and so forth)
            Message_ID = str(msg.get('Message-ID'))
            
            #print "\tTO: " + str(TO_str) + "\tFROM: " + str(FROM_str) +"\tFileSize = %0.7f MB" % (filesize/(1024*1024.0)) +"\tPath:" + str(filepath)
            Sort_append()
            
            cur.execute("INSERT INTO Pidgeon_Nest VALUES ('"+ data_md5 +"','"+ UniqIdent +"','"+ TO_str +"','"+FROM_str+"','"+Message_ID+"','"+str(filepath)+"') ")        
            #register filepath for the individual file, for later database logging //////


            if unique_ID_dict.has_key(UniqIdent) :
                    ##id exists, submit to sqlite database"##update database via UPDATE
                cur.execute("UPDATE correspondence_map SET count=count+1 WHERE md5_hash='"+data_md5+"'")
            else:
                    ##"Field does not exist" , append to dictionary"
                unique_ID_dict[UniqIdent] = data_md5        
                    ##append to sql database and set count to 1"
                cur.execute("INSERT INTO correspondence_map VALUES ('1','"+ TO_str +"','"+ TO_ID +"','"+ FROM_str +"','"+ FROM_ID +"','"+ data_md5 +"')")
                 
            conn.commit()
            filepath = os.path.abspath(filepath)
            #count each file processed amount of loops (files handled)
            mailcounter += 1

def Sqlconnection():
    global conn
    global cur
    conn = sqlite3.connect("PigeonLoft.db")
    cur = conn.cursor()

def SqlCreateTable():
    cur.execute("CREATE TABLE IF NOT EXISTS Pidgeon_Nest (md5_hash,UniqIdent,m_from, m_to,Message_ID,m_filename)")
    conn.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS correspondence_map (count,to_m,to_uniqueNumber,from_m,from_uniqueNumber,md5_hash)")
    conn.commit()
    
def processDirectory ( args, dirname, filenames ):
    global path                            
    path = dirname
    dataextraction()

Sqlconnection()
SqlCreateTable()
os.path.walk(top_level_dir, processDirectory, None)


print "\nFinished!\n"    + "\t  Files processed:" + str(mailcounter) +"\t\tData processed:%0.2fMB" % (folder_size/(1024*1024.0)) + "\t\tNumber of Lines:" + str(numlines)  +"\n"

