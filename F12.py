# "r" - Read
f = open("Ruturaj.txt", "r")
data = f.read()
f.close()

# "w" - Write
f = open("Ruturaj.txt", "w")
f.write("Writing new content")
f.close()
