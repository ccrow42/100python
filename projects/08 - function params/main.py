alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# This could have been a single function. We could have made the shift number negative by simply multiplying by -1
def encrypt(text, shift):
    # display could have been a string, use += to append (it isn't just for math!)
    display = []
    for char in text:
        # A better way to do this would have been to see if the letter was 'in' the alphabet and ignore it if not
        if char == " ":
            display.append(" ")
        # So this is still required because we only have 25 indecies. In the solution, she duplicated, so there are 51.
        # Remember: .index() returns the first index number if there are multple values
        elif (alphabet.index(char) + shift) > 25:
            display.append(alphabet[alphabet.index(char) + shift - 26])
        else:
            display.append(alphabet[alphabet.index(char) + shift])
    # This join isn't required if we had used a string instead of an array
    print("".join(display))

def decrypt(text, shift):
    display = []
    for char in text:
        if char == " ":
            display.append(" ")
        elif (alphabet.index(char) - shift) < 0:
            display.append(alphabet[alphabet.index(char) - shift + 26])
        else:
            display.append(alphabet[alphabet.index(char) - shift])
    print("".join(display))
run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Type your message:\n").lower()
    input_shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(input_text, input_shift)
    elif direction =="decode":
        decrypt(input_text, input_shift)
    else:
        run_again == False
    


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 