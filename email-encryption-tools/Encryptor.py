def encryptor():
    # Lists of encrypting characters
    charList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                 "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "~", "!", 
                "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
             "{", "}", "|", ":", "<", ">", "?", "-", "=", "[", "]", ";",
            "'", ",", ".", "/", " "]

    charListEncrypted = ["z", "x", "v", "t", "r", "p", "n", "l", "j", "h", "f", "d", "b", "a", "c",
                            "e", "g", "i", "k", "m", "o", "q", "s", "u", "w", "y", "Z", "X", "V", "T", 
                            "R", "P", "N", "L", "J", "H", "F", "D", "B", "A", "C", "E", "G", "I", "K", 
                            "M", "O", "Q", "S", "U", "W", "Y", "2", "4", "6", "8", "0", "9", "7", "5", "3", "1",
                            " ", "/", ".", ",", "'", ";", "]", "[", "=", "-", "!", "~", "#", "@", "%", "$", "&", "^",
                            "(", "*", ")", "?", ">", "<", ":", "|", "}", "{", "+", "_"]

    # To check the correctness of the charList
    if len(charList) == len(charListEncrypted): 

        # Prompt user to input the message to be encrypted
        msg = input("Message to be encrypted: ")
        
        result = ""
        for i in range(len(msg)):
            if msg[i] in charList:
                result += charListEncrypted[charList.index(msg[i])] # Encrypt input char by corresponding encrypting char 
                i += 1
            else:
                i += 1

        print("\n" + result + "\n")
        
        # Temporary solution for invalid keys entered
        print("*** Caution: Please do not enter any keys other than the choices indicated below or the program will be terminated! ***")
        choice = input("Do you want to decrypt the message?: Y/N ")

        if choice == "Y" or choice == "y":
            decrypted = ""
            for j in range(len(result)):
                if result[j] in charListEncrypted:
                    decrypted += charList[charListEncrypted.index(result[j])]
                    j += 1
                else:
                    j += 1
            
            if decrypted == msg:
                return decrypted
            else:
                return "An error occured. The program will be terminated."

        elif choice == "N" or choice == "n":
            return "\n" + result + "\n"
        else:
            print("Invalid key entered, the program will be terminated.")

    else:
        return "An error occured. The program will be terminated."

print(encryptor())
