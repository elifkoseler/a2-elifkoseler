from hashlib import sha256

def create_hash(password):                  ###########################################################
    pw_bytestring = password.encode()       # This part is taken from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
    return sha256(pw_bytestring).hexdigest() ##########################################################

def true_password(hsh2):
  if(hsh1 == hsh2):
    return 1
  else:
    return 0

pw1 = input('Please enter your password:')
hsh1 = create_hash(pw1)

mylist = []
def take_input():
  what = true_password(hsh2)
  if(what):
    mylist.append(myvalue)
    print("Previously entered comments:")
    for comment in mylist:
      i = mylist.index(comment)
    
      print(i+1,"-",comment)
  else:
    print("I am sorry I can't let you do that.")
    
while(1):
  myvalue = input("Enter your comment: \n")
  pw2 = input('Enter your password:\n')
  hsh2 = create_hash(pw2)
  take_input()
  
  
