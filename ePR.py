'''
Created on 24/08/2012
@author: litek
'''
#!/usr/bin/env python


#imports listed here. #Email.message is used so i can call the email.message_from_string() parsing function     #email.utils is used so i can call the get_all() function to extract FROM and TO fields from the Email
import email


    #allow regular expressions (for email extration process)
#import re

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
conn = ""                       #sqlite connection for the memory db 
cur = ""                        #sqlite curser for the memory db
conn1 = ""                      #sqlite connection for the fileDB
cur = ""                        #sqlite curser for the fileDB
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

def correspondence_plotter():
    import Gnuplot
    gp = Gnuplot.Gnuplot()
    gp('set datafile separator "|"')
    gp('set term jpeg medium size 1000,1000')
    gp('set output "correspondence_map.jpeg"')    
    gp('set grid')
    gp('set xlabel "TO:"')
    gp('set ylabel "FROM:"')
    gp('set xtics rotate')
    #'[0:25][0:25]"<...
    gp.plot('[0:25][0:25]"< sqlite3 PidgeonLoft.db  \'select * from correspondence_map\'"using 5:3:(log($1)):xtic(4):ytic(2) title "Corrospondence plot" with circles,""using 5:3:1 with labels title" ')


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
            
            '''
            testing a sorting mechanism..of sorts
            '''
            if "Your mailbox has exceeded one or more size limits set by your" in mailfile:
                continue
            
            #Parse imported file to a format get_all() can handle
            msg = email.message_from_string(mailfile)

                #if file checked returns None(no email address in To), skip to next file(loop)
            if msg.get('To') is None:
                continue 
            
                #if file checked returns None(no emails address in FROM), skip to next file(loop)
            if msg.get('From') is None:
                continue
            
            
                #enumerate amount of lines in file # move the counter to here, there is now need to count files if they dont countain any To: fields etc [the above check]
            for lines in open(filepath):
                numlines += 1
            
            
            #get current filesize and put it into filesize var, append current filesize to folder_size to count amount of data
            filesize = os.path.getsize(filepath)
            folder_size += filesize
            
            #this works with Eclipse execution, but not when done from shell, must be something todo with ...rwareeararar .. unicode specification in'app wise
            filepath = filepath.encode('ascii', 'replace')           
            #Get wanted fields via msg.get(), use regular expressions to remove unnessasarry gunk,stuff and poop, then print results.        
            #TO_str = re.findall(r"([\w\-\._0-9]+@[\w\-\._0-9]+)",  str(msg.get('To')), re.UNICODE)[0]        
            #FROM_str = re.findall(r"([\w\-\._0-9]+@[\w\-\._0-9]+)", str(msg.get('from')), re.UNICODE)[0]
            #print str(filepath) Just for debugging
            TO_str = str(msg.get('To'))     
            FROM_str = str(msg.get('from'))
            
            
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
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

def SqlCreateTable():
    cur.execute("CREATE TABLE IF NOT EXISTS Pidgeon_Nest (md5_hash,UniqIdent,m_to,m_from,Message_ID,m_filename)")
    conn.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS correspondence_map (count,to_m,to_uniqueNumber,from_m,from_uniqueNumber,md5_hash)")
    conn.commit()


def Sqlconnection1():
    global conn1
    global cur1
    conn1 = sqlite3.connect("PidgeonLoft.db")
    cur1 = conn.cursor()



def processDirectory ( args, dirname, filenames ):
    global path                            
    path = dirname
    dataextraction()




Sqlconnection()
SqlCreateTable()



os.path.walk(top_level_dir, processDirectory, None)


Sqlconnection1()
#SqlCreateTable1() Does not seem to be needed because its a direct dump
query = "".join(line for line in conn.iterdump())
conn1.executescript(query)

correspondence_plotter()

#os.remove("PidgeonLoft.db")    

print "\nFinished!\n"    + "\t  Files processed:" + str(mailcounter) +"\t\tData processed:%0.2fMB" % (folder_size/(1024*1024.0)) + "\t\tNumber of Lines:" + str(numlines)  +"\n"

