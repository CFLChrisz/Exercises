
'''
“print” treats the % as a special character you need to add, so it can know, that when you type “f”,
the number (result) that will be printed will be a floating point type,
and the “.2” tells your “print” to print only the first 2 digits after the point.
'''

d = 9999
print (("Value: %.2f" % float(d)),'$')