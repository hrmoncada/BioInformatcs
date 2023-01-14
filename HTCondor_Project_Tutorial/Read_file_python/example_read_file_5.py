# http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/
f = open('history.txt')
for line in iter(f):
    print line
f.close()
