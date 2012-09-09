import hashlib
import cPickle as pickle

FROM_STR = "ames@gogo.com"
TO_STR = "Bam@doomr.us"

data = [FROM_STR,TO_STR]
data_pickle = pickle.dumps(data)
data_md5 = hashlib.md5(data_pickle).hexdigest()
print data_md5