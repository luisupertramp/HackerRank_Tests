import fileinput

def textEditor(text) : 

    textString = []
    undoStack = []
    
    def switch(command, textString, undoStack, fromUndo) :
        # 1. Append new string
        if command[0] == '1' :
            textString += list(command[1]) 
            
            # we add the undo command to the undoStack
            if not fromUndo :
                undoStack.append('2' + ' ' + str(len(command[1])))

        # 2. Delete K last chars
        elif command[0] == '2' :
            # we add the undo command to the undoStack first
            if not fromUndo :
                undoStack.append('1' + ' ' + ''.join(textString[len(textString)-int(command[1]):]))

            # then delete the chars
            del textString[-int(command[1]):]

        # 3. Print the Kth character
        elif command[0] == '3' :
            print(textString[int(command[1])-1])
        
        # 4. Undo
        elif command[0] == '4' :
            # process the command line and call switch again
            line = undoStack.pop().replace("\n", "").split()
            switch(line, textString, undoStack, True)

        # Command not recognized
        else :
            print("ERROR, command not found")
            return
    
    for i, line in enumerate(text) :
        if i != 0 :
            line = line.replace("\n", "").split()
            switch(line, textString, undoStack, False)

f = open("textEditor-testCase.txt", "r")
textEditor(f)