##Take emails and sort them alphabethical
##Generate MD5 hash for display in plot (indirect Data Anonymization)

import hashlib
import cPickle as pickle
data_md5 = ""
contactjoin = ""

unique_ID_dict = {}

def Sort_append():
    FROM_STR = "bam@doomr.us"
    TO_STR = "ames@gogo.com"
    
    global contactjoin
    global data_md5
    if FROM_STR < TO_STR:
        contactjoin = FROM_STR + "__" + TO_STR
        data = [contactjoin]
        data_pickle = pickle.dumps(data)
        data_md5 = hashlib.md5(data_pickle).hexdigest()

    else:
        #concatenate strings for ID-String
        contactjoin = TO_STR + "__" + FROM_STR
        #Generate MD5 Hash for the MD5-Hash.
        data = [contactjoin]
        data_pickle = pickle.dumps(data)
        data_md5 = hashlib.md5(data_pickle).hexdigest()

    
    if unique_ID_dict.has_key(contactjoin) :
        print "id exists, submit to sqlite database"
        print "update count field for UniqIdent in database with 1"
        print "sql = UPDATE myTable SET Column1=Column1+1"
    else:
        print "Field does not exist"
        print "append to dictionary"
        unique_ID_dict[contactjoin] = data_md5        
        print "append to sql database and set count to 1"
    
Sort_append()
print "\t" + str(unique_ID_dict.items())

print ""
print ""

Sort_append()
print "\t" + str(unique_ID_dict.items())

#print "ID-String: " + contactjoin
#print "MD5-Hash: " + data_md5
