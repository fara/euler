import datetime
import hashlib
from random import Random


def hash(s):
    return int(hashlib.sha1(s).hexdigest(), 16)

def bits_set(d):
    r = d
    while True:
        d = d >> 1
        r = r - d
        if not d:
            return r

def distance(s1, s2):
    return bits_set(hash(s1)^hash(s2))
   
def swap(remaining, ordered=[]):
    """Recursively swap words."""
    for i in xrange(len(remaining)):
        remaining2 = remaining[:]
        ordered2 = ordered + [remaining2.pop(i)]
        if len(remaining2) > 0:
            for words in swap(remaining2, ordered2):
                yield words
        else:
            yield ' '.join(ordered2)

           
# START           
       
start = datetime.datetime.now()       
print start
       
challenge = "I would much rather hear more about your whittling project"

t_dict = "beta betas bford template tender tesler tests scala portable solo flex scalable rubyonrails rails cloud web hosting ec2 ar berners tdd tech technical pixel plugin poe polybius pop3 pops scale sccs schema schneier scope"
dict = t_dict.split(' ')

first = ' '.join(dict[:12])
min = distance(challenge, first)
print first
print min

tests = 0

for i in range(22):
    for p in swap(dict[i:i+12]):
        p = p + ' baudi' #+ ''.join( Random().sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 5) )
        d = distance(challenge, p)
        tests = tests + 1

        if d < min:
            min = d
            print "---"
            print p
            print min

finish = datetime.datetime.now()   
print finish
print tests, " pruebas en ", (finish - start)