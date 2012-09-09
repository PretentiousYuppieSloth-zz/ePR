##Take emails and sort them alphabethical
##Generate MD5 hash for display in plot (indirect Data Anonymization)

import hashlib
import cPickle as pickle
data_md5 = ""
contactjoin = ""
def Sort_append():
    #FROM_STR = "ames@gogo.com"
    #TO_STR = "bam@doomr.us"
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

        
Sort_append()
print "ID-String: " + contactjoin
print "MD5-Hash: " + data_md5
