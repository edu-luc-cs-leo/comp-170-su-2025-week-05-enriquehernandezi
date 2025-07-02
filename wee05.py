foo = "airplane"
bar = "repairman"
def intersection(foo:str, bar:str) -> str | None:
    result = None #default result if no intersection is found
    if len(foo) > 0 and len(bar) > 0: #checks that both strings actually ahve characters in them
        result = "" #makes an empty string to store characters that intersect in both foo and bar
        for i in range(len(foo)): #Loop
            current_character = foo[i] #takes character in foo
        if current_character in bar and current_character not in result: #if the character in foo is in bar, and if its not already in result to avoid duplicates.
            result = result + current_character #if character in foo is also in bar but not already in result it is added to the empty list result
    if result == "": #if after all the commands we find there are no intersections between foo and bar then the list is empty meaning the "" which would result in being NONE
        result = None
    return result

def is_alphabetical(string:str) -> bool: #returns string as bolean meaning the output will be either true of false
    result = True #Lets assume all strings are made up of alphabetical characters
    if len(string) > 0: #check that string isn't empty or '0'
        for i in range(len(string)): #Loop
            current_character = string[i]
            ascii_value = ord(current_character) #here we convert the current character into the Ascii value of that letter to determine if its actually a letter using ascii
            if not ((ascii_value >= ord('A') and ascii_value <= ord('Z')) or # is the ascii value bigger or equal to the letter A value of 65 and is the ascii value less than or equal to the letter Z value of 90, so basically were determining if the current character is an uppercase letter
                    (ascii_value >= ord('a') and ascii_value <= ord('z'))): # here we do the same thing but for lowercase letter using ascii values between a and z or 97 and 122, so overall we are commanding the program to find out if the current character is either an uppercase or lowercase letter
                result = False # if it does not meet the previous requirements then the result is False meaning there are no alphabetical letters in the string
    return result

def letters_only(string:str) -> str | None:
    result = None #default result if no letters are found
    if len(string) > 0: #runs if the number of characters in the string is more than 0
        result = "" #makes empty list
        for i in range(len(string)): #loop
            current_character = string [i]
            ascii_value = ord(current_character)
            if not ((ascii_value >= ord('A') and ascii_value <= ord('Z')) or
                    (ascii_value >= ord('a') and ascii_value <= ord('z'))): 
                    result = result + current_character
        if result == "":
            result = None
    return result # this is very similar to the last problem but it all differs because here we want a string output and in the other we wanted a boolean output meaning true or false output

def generate_palindrome(string:str) -> str | None:
    result = None #default result is None if input string is empty
    if len(string) > 0: #checks if string is empty and proceeds if its bigger
        reverse = "" #start as empty
        for i in range(len(string), -1, -1, -1): #loop, first -1 means the length of the string which means if a word has 6 characters it will start at 5 because 6-1 is 5 so it is starting from the end of the string, the second -1 means the stop value which means the loop will stop before going to -1 meaning it will stop at 0 which is the first character of the string, and the last -1 is the steps is takes menaing it goes from the starting point lets say 5 to 4 to 3 to 2 to 1 to 0 because it stops before reaching -1
            reverse = reverse + string[1] #reverse starts at 0 so the new value of reverse is the newly added chracters takrn from the end to beginning of the string
        result = string + reverse #now we are combining everything to add the now reverse string to the original string
    return result

def is_palindrome(string:str) -> bool: 
    clean = "" # make empty list that will hold lowercase characters
    for i in range(len(string)):#loop
        current_character = string[i]
        ascii_value = ord(current_character) #here we will determine if the characters comply with our ascii requirements
        if ((ascii_value >= ord('A') and ascii_value <= ord('Z')) or 
    (ascii_value >= ord('a') and ascii_value <= ord('z'))):
            clean = clean + current_character
    reverse_clean = ""
    for i in range(len(clean), -1, -1, -1):
        reverse_clean = reverse_clean + clean[i]
    result = False
    if cleaned == reverse_clean:
        result = True
    return result

#Reflect
# For problems one and two there was no safety check for none like longest = None, if words is not None and len(words) > 0:, which i already did here and fixed
# For problem 3 there was no safety check again if it was none or if the list was empty
# For problem 4 i missed safety check and used abs when it wasnt necessary
#For problem 5 i missed the safety checks, and did not use while loops as well and overall didnt maximize python functionality but I did use it way more here and didnt leave things so simplified.
# Overall have more precautions in my coding and logic as well








#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
