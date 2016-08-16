x = 0

for date in open("date.txt", "r").readlines():
    #print "Orig: " + date
    #print "New: " + date.split()[0] + " " + date.split()[1] + " " + str(int(date.split()[2])+1)
    date = date.split()[0] + " " + date.split()[1] + " " + str(int(date.split()[2])+1) + "\n"
    print date
    if date in open("fridays.txt", "r").readlines():
        print "yes!"
        x += 1
    else: print "no..."


print x
