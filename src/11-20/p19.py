# You are given the following information, but you may prefer to do some research for yourself.
#    * 1 Jan 1900 was a Monday.
#    * Thirty days has September,
#      April, June and November.
#      All the rest have thirty-one,
#      Saving February alone,
#      Which has twenty-eight, rain or shine.
#      And on leap years, twenty-nine.
#    * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

count = 0
dow = 1
for year in range(1900, 2000+1):
    for month in range(1, 12+1):
        days = 31
        if month == 4 or month == 6 or month == 9 or month == 11:
	        days = 30
        if month == 2:
		    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			    days = 29
		    else:
			    days = 28
        if dow == 7 and year >= 1901:
		    print "Sunday 1", month, year
		    count += 1
        dow = ((days + dow) % 7) + 1
			
			
print count