stack = list()
maxsize = int(input("Enter the Stack MaxSize:"))

def isempty():
  top = len(stack)
  if(top==0):
    print("Stack is Empty now.\n")
   
  elif (top==maxsize):
    print("Stack is Full\n")



def push_item():
  top = len(stack)  
  for i in range(maxsize):
    stack.append(int(input(f"{i}th items:")))
  top += 1
  isempty()
    





def pop_item():
  top = len(stack)
  for i in range(top-1,-1,-1):
     if(top==-1):
       print("\nStack is Empty")
     else:
       item = stack.pop(i)
       print(f"{i}th Popped Item: {item}\n")
  isempty()


      
 

isempty()
push_item()

pop_item()

