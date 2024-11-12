# "ab" - Append in Binary
f = open("Ruturaj.txt", "ab")
f.write(b"\nBinary append")
f.close()

# "xb" - Exclusive creation in Binary
f = open("Ruturaj_binary.txt", "xb")
f.write(b"Binary exclusive creation")
f.close()