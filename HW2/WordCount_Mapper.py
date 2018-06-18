import sys

words = ['Dec', 'Chicago', 'Java', 'hackathon']
 
for line in sys.stdin:
    
    line = line.strip()
    line = line.lower()
    
    for word in words: 
        word2 = word.lower()
        if word2 in line:
            print '%s\t%s' % (word, "1")
        elif word2 not in line:
        	print '%s\t%s' % (word, "0")