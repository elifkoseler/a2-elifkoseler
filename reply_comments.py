mylist = []

def take_input():
  myvalue = input("Enter your comment: \n")
  mylist.append(myvalue)
  
  print("Previously entered comments:")
  for comment in mylist:
    i = mylist.index(comment)
    
    print(i+1,"-",comment)

while(1):
  take_input()
