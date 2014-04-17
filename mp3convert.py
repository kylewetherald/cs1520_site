import base64
import sys
# pick sound file you have in working directory
# or give full path
sound_file = sys.argv[1]
# use mode = "rb" to read binary file
fin = open(sound_file, "rb")
binary_data = fin.read()
fin.close()
# encode binary to base64 string (printable)
b64_data = base64.b64encode(binary_data)
print b64_data