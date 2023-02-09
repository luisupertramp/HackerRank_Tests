def caesarCipher(s, k):
    cipherText = []

    for letter in s :
        # * ord() and chr() take advantage of the indexation of ASCII characters so I don't have to ...
        # * ... worry about creating individual indexed lists for the alphabet.

        # If the rotation of letters is greater than the amount of letters in the alphabet which is 26 ...
        if k > 26 :
            #  simplify by dividing K by 26
            kTimes, trash = divmod(k / 26, 1)
            k = int(k-kTimes*26)
            
        newPosition = ord(letter) + k

        if letter.isalpha() :

            if letter.isupper() :
                # ASCII upper letters goes from 65 to 90
                if newPosition > 90 :
                    newPosition = newPosition - 90 + 64

                cipherText.append(chr(newPosition))

            elif letter.islower() :
                # ASCII lower letters goes from 97 to 122
                if newPosition > 122 :
                    newPosition = newPosition - 122 + 96

                cipherText.append(chr(newPosition))

        else : 
            cipherText.append(letter)

    print(''.join(cipherText))

caesarCipher('www.abc.xy' , 87)