def isBalanced(s):
    # Write your code here
    bracketsList = list(s)
    pendingBrackets = []

    isBalanced = True

    for i in range(int(len(bracketsList))):

        # check if current bracket opens
        if bracketsList[i] == '{' or bracketsList[i] == '[' or bracketsList[i] == '(' :
            # if the last bracket opens, return NO
            if i == len(bracketsList)-1 :
                return 'NO'
            
            # and apppend the current opening bracket to a debt list
            pendingBrackets.append(bracketsList[i])

        # check if the bracket closes and compare to the last one in debt list
        else :
            # if the first bracket closes, immediately returns NO
            if i == 0 :
                return 'NO'
            
            # specify the corresponding opening bracket
            if bracketsList[i] == '}' :
                oppositeBracket = '{'
            elif bracketsList[i] == ']' :
                oppositeBracket = '['
            elif bracketsList[i] == ')' :
                oppositeBracket = '('

            # if the closing bracket belongs to the last in debt, remove the last one
            if pendingBrackets and pendingBrackets[-1] == oppositeBracket :
                pendingBrackets.pop()
            else :
                return 'NO'

    return 'YES'

# print(isBalanced('{{}('))
# print(isBalanced('[]([{][][)(])}()([}[}(})}])}))]](}{}})[]({{}}))[])(}}[[{]{}]()[(][])}({]{}[[))[[}[}{(]})()){{(]]){]['))
# print(isBalanced('{()({}[[{}]]()(){[{{}{[[{}]{}((({[]}{}()[])))]((()()))}(()[[[]]])((()[[](({([])()}))[]]))}]})}'))
# print(isBalanced('()(){{}}[()()]{}{}'))
# print(isBalanced('{}()([[]])({}){({[][[][[()]]{{}[[]()]}]})}[](())((())[{{}}])'))
# print(isBalanced('{}(((){}){[]{{()()}}()})[]{{()}{(){()(){}}}}{()}({()(()({}{}()((()((([])){[][{()}{}]})))))})'))
# print(isBalanced('][[{)())))}[)}}}}[{){}()]([][]){{{{{[)}]]{([{)()][({}[){]({{'))
# print(isBalanced('{[{((({}{({({()})()})[]({()[[][][]]}){}}))){}}]}{}{({((){{}[][]{}[][]{}}[{}])(())}[][])}'))
# print(isBalanced('()[[][()[]][]()](([[[(){()[[]](([]))}]]]))'))

