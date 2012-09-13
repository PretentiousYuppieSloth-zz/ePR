#http://www.roman10.net/named-pipe-in-linux-with-a-python-example/


#this shit might be broken, check out link
import time,os, tempfile

tmpdir = tempfile.mkdtemp()
filename = os.path.join(tmpdir, 'myfifo')

print filename

try:
    os.mkfifo(filename)
except OSError, e:
    print "Failed to create FIFO: %s" % e
else:
    time.sleep(5)
    fifo = open(filename, 'w')
    # write stuff to fifo
    print >> fifo, "hello"
    fifo.close()
    os.remove(filename)
    os.rmdir(tmpdir)
