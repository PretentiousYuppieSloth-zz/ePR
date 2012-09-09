#!/usr/bin/python
#http://www.tutorialspoint.com/python/python_dictionary.htm
#https://yuji.wordpress.com/2008/05/14/python-basics-of-python-dictionary-and-looping-through-them/

# if we use dict instead of lists, we can store the md_hash in relation to the UniqIdentifier. 

##create dictionary
dict_test = {'Name': 'sloth', 'Age': 99, 'Class': 'First'};

print "dict_test['Name']: ", dict_test['Name'];
print "dict_test['Age']: ", dict_test['Age'];

## Append to dictionary
dict_test['Sex'] = "Girl"

print dict_test.keys()


## Delete from Dictionary
del dict_test['Name']

## check if a specific key is in the dictionary
print ""
print "Value Age: %s" %  dict_test.has_key('Age')
print "Value Sex: %s" %  dict_test.has_key('Sex')
print "Value sex: %s" %  dict_test.has_key('sex')

## Conditional check
print ""
if dict_test.has_key('Name') :
    print "dict_test['Name']: ", dict_test['Name'];
else:
    print "Field does not exist"



##update field if it exists, or add field to the collection
print ""
dict_test['Age']+=1  # updates if 'a' exists, else adds 'a'
print "dict_test['Age']: ", dict_test['Age'];


## print items in dirt
print ""
for key, value in dict_test.iteritems():
    print "%s-%s" % (key, value)
