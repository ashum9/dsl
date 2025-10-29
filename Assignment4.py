# impliment real time undo/redo system for text editing app.using stack 
# The system should support the following op;
# make a change = A new change to the document is made
# undo action 
# redo
# Display document state

class Stack:
    def __init__(self):
        self.stack= [" "]
        self.pointer = 0

    def do (self,action):
        curr = self.stack[self.pointer]
        update = curr + action

        self.stack = self.stack[:self.pointer +1]
        self.stack.append(update)
        self.pointer+=1
        print(f"Add {action} => current state : {update}")

    def undo(self):
        if self.pointer==0:
            print("nothing to undo")
            return
        self.pointer-=1
        print(f"Current text: {self.stack[self.pointer]}")
    
    def redo(self):
        if self.pointer+1 >= len(self.stack):
            print("Nothing to redo")
            return 
        self.pointer+=1
        print (f"Current text {self.stack[self.pointer]}")

s = Stack()

while (True):
    print("1.ADD    \n2.UNDO  \n3.REDO  \n4.Exit")
    operation = int(input("Enter the number operation you want to preform: "))
    if(operation==1):
        word = input("Enter a word: ")
        s.do(word)
    if(operation==2):
        s.undo()
    if(operation==3):
        s.redo()
    if(operation==4):
        print ("You have exited successfully")
        break