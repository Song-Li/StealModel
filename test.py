from file_base import ReadFile

r = readFile("try")
counts = r.getTokenCounts("terrier-stop.txt", "\r\n")
for c in counts:
    if counts[c] != 0:
        print c,counts[c]
