# "rb" - Read in Binary
f = open("Ruturaj.txt", "rb")
data = f.read()
f.close()

# "wb" - Write in Binary
f = open("Ruturaj.txt", "wb")
f.write(b"Binary content")
f.close()