import sys

pages_PR = {}
pages_SR = {}

for line in sys.stdin:

    line = line.strip()
    ThisKey, val = line.split('\t')
    
    
    if "0." in val:
        source, pr = val.split(",")
        
        try:
            pr = float(pr)
            pages_PR[ThisKey] = pages_PR.get(ThisKey, 0) + pr
        except ValueError:
            pass
    
    else:
        outlinks = val
        try:
            pages_SR[ThisKey] = outlinks
        except ValueError:
            pass

for key in pages_PR:
    print '%s\t%s' % (key, pages_SR[key] + " "+ str(pages_PR[key]))