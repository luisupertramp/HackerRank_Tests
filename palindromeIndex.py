def palindromeIndex(s):
    # Write your code here
    def isPalindrome(word) :
        reverseWord = list(word)
        reverseWord.reverse()

        if word == ''.join(reverseWord) :
            return True

    if isPalindrome(s) :
        # print('Already is palindrome')
        return -1

    for i in range(int(len(s)/2)) :
        charToRemove = 0

        # If opposites are not equal...
        if s[i] != s[len(s)-1-i] :

            # Check if rather, the char in the far left is equal to the char in the far right -1
            # ... or if the char in the far right is equal to the char in the far left +1
            if s[i] == s[len(s)-2-i] or  s[i+1] == s[len(s)-1-i] :

                # If the char in the far left is equal to the char in the far right -1
                if s[i] == s[len(s)-2-i] :
                    # ... save the character from the far right to remove
                    charToRemove = len(s)-1-i
                    possibleText = s[:charToRemove] + s[charToRemove+1:]

                    # Test if it is a palindrome with the possible text
                    if isPalindrome(possibleText) :
                        # print(charToRemove)
                        return(charToRemove)
                        break
                    
                # If the char in the far right is equal to the char in the far left +1
                if s[i+1] == s[len(s)-1-i] :
                    # ... save the character from the far left to remove
                    charToRemove = i
                    possibleText = s[:charToRemove] + s[charToRemove+1:]

                    if isPalindrome(possibleText) :
                        # print(charToRemove)
                        return(charToRemove)
                        break
            
            # ... otherwise it means that there is no way to create a palindrome by removing only one character
            else : 
                # print('This word can't be palindrome')
                return -1


# palindromeIndex('aaab')
# palindromeIndex('xzaaaxz')
# palindromeIndex('aaa')
# print(palindromeIndex('hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh'))
