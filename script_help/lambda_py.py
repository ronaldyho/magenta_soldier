# Convert nextline to something else
x = lambda a : a.replace("\n", " ")

# Convert spaces to something else 
x = lambda a : a.replace("&nbsp;", "")

#####
z = open("change.txt", 'r')
x(z.read())
