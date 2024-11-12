# "a" - Append
f = open("Ruturaj.txt", "a")
f.write("\nAppending more content")
f.close()

# "x" - Exclusive creation
f = open("Ruturaj_new.txt", "x")
f.write("Creating a new file")
f.close()
