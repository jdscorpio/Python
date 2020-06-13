import hashlib

def hash_file(filename):
    h = hashlib.sha1()
    with open(filename,'rb') as file:
       temp = 0
       while temp !=b'':
           temp = file.read(1024)
           h.update(temp)
    return h.hexdigest()

txt = hash_file("calendar.py")
print(txt)
