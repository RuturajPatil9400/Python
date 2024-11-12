# "r+" - Read and Write
f = open("Ruturaj.txt", "r+")
data = f.read()
f.write("\nAdding content after reading")
f.close()

# "w+" - Write and Read
f = open("Ruturaj.txt", "w+")
f.write("Writing and reading")
f.seek(0)
data = f.read()
f.close()