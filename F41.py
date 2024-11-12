# "a+" - Append and Read
f = open("Ruturaj.txt", "a+")
f.write("\nAppending and reading")
f.seek(0)
data = f.read()
f.close()
