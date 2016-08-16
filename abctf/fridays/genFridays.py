months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
thirtydays = ["September", "April", "June", "November"]

y = 7 #init
for x in xrange(0,20):
    year = "200" + str(x)
    #print year
    for month in months:
        #print month
        while y < 32:
            if y == 31 and month in thirtydays:
                y = y % 30
                break
            else:
                
