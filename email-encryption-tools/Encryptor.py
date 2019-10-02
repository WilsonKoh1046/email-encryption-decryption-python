def encryptor():

    # Lists of encrypting characters
    charList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                 "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", 
                "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
            "~", "{", "}", "|", ":", "<", ">", "?", "-", "[", "]", ",",
            ".", ";", " "]
    charListEncrypted = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
            "~", "{", "}", "|", ":", "<", ">", "?", "-", "=", "[", "]", ",",
            ".", "!!", "@@", "##", "$$", "%:%", "^^", "&&", "**", "((", "))", "__", "++", "~~", "{:{",
            "}:}", "||", "::", "<<", ">>", "??", "--", "==", "[[", "]]", ",,", "..",
             "...", ",,,,?", "///}{[", "^&%", "()&%^$:", "$%#$@#@!", ":(*&<)", "--++!", "@%^&$#$@!!", "?/)^%#@@",
             ";", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]

    # Prompt user to input the message to be encrypted
    msg = input("message to be encrypted: ")
    
    result = ""
    for i in range(len(msg)):
        if msg[i] in charList:
            result += charListEncrypted[charList.index(msg[i])] # Encrypt input char by corresponding encrypting char 
            i += 1
        else:
            i += 1

    print("\n" + result + "\n")
    # To check the correctness of the char list
    print(len(charList))
    print(len(charListEncrypted))

    choice = input("Do you want to decrypt the message?: Y/N ")

    if choice == "Y" or choice == "y":
        decrypted = ""
        for j in range(len(result)):
            if result[j] in charListEncrypted:
                decrypted += charList[charListEncrypted.index(result[j])]
                j += 1
            else:
                j += 1

        return decrypted
    else:
        return result

print(encryptor())
