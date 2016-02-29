# Your task has been made easy, as the encryption key consists of three lower case 
# characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file 
# containing the encrypted ASCII codes, and the knowledge that the plain text must 
# contain common English words, decrypt the message and find the sum of the ASCII 
# values in the original text.
file = open("cipher1.txt")

# go

chr_vec = {}
pos = 0
phrase = ""			
for line in file:
	chars =  line.split(',')
	for char in chars:
	    if pos % 3 == 0:
			phrase = phrase + chr(int(char)^ord('g'))		
	    if pos % 3 == 1:
			phrase = phrase + chr(int(char)^ord('o'))		
	    if pos % 3 == 2:
			phrase = phrase + chr(int(char)^ord('d'))		
			
	    if pos % 3 == 2:
	        if char in chr_vec:
		        chr_vec[char] = chr_vec[char] + 1
	        else:
	            chr_vec[char] = 1
	    pos += 1


for ch in chr_vec:
    print ch, chr_vec[ch]
	
print phrase

sum = 0	
for c in phrase:
    sum += ord(c)
print sum