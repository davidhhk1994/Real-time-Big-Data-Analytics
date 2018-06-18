# Counting the occurances of specific search terms in a multiple line file

name = input('Enter name of the text file: ')+'.txt'

with open(name, 'r') as f:
    lines = f.read().split("\n")
    
for line in lines:
    print(line)
print("Number of lines is {}".format(len(lines))) 

output = open("HW2_p5_output.txt", "w")

word = input("input your word: ") 

for w in word: 
	count=0
	w2=w.lower()
	for line in lines:
		line=line.lower()
		if w2 in line: 
			count += 1
	print >> output, "{} : {}".format(w, count)

output.close()

