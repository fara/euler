import sys, urllib, re

#url = sys.argv[1]
url = "http://www.google.com"
instream = urllib.urlopen(url)
page = instream.read()
instream.close()

links = re.findall(r'href=\"[^\"]+\"', page)
temp = set()
for x in links:
    x = x[6:-1]    # strip off 'href="' and '"'
    if x.startswith('http://'):
        temp.add(x)
        print x
links = list(temp)
links.sort()
for x in links:
    print x
