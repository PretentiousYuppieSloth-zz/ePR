import os


def processDirectory ( args, dirname, filenames ):                              
    print 'Directory',dirname                                                   
    for filename in filenames:                                                  
       print "\t" + dirname + "/" + filename
    print "\n"                                            
                                                                                
top_level_dir = "."                                                    
os.path.walk(top_level_dir, processDirectory, None )                            
                                                                                
##os.path.walk() works with a callback: processDirectory() will be              
##called for each directory encountered.
