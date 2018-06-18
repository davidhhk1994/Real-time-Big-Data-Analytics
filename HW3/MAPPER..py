import sys

for line in sys.stdin:
	
    line = line.strip()
    data = line.split(" ")

    PR = data[-1]
    source = data[0]
    dest = data[1:-1]
    share = float(PR) / float(len(dest))

    for i in range(len(dest)):
        print '%s\t%s' % (dest[i], source + ", " + str(share))

    print '%s\t%s' % (source, " ".join(dest))

    