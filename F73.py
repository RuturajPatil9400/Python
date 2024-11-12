# "rb+" - Read and Write in Binary
f = open("Ruturaj.txt", "rb+")
data = f.read()
f.write(b"\nBinary read and write")
f.close()

# "wb+" - Write and Read in Binary
f = open("Ruturaj.txt", "wb+")
f.write(b"Binary write and read")
f.seek(0)
data = f.read()
f.close()

# "ab+" - Append and Read in Binary
f = open("Ruturaj.txt", "ab+")
f.write(b"\nBinary append and read")
f.seek(0)
data = f.read()
f.close()