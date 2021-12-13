'''morse code translator by Hocian (Hoccyy on Github)
   Support me by following me on github! it means a lot! https://github.com/Hoccyy
   Follow me to encoruage me to make more projects!
'''
from datetime import datetime
import webbrowser as wb

# Morse-code alphabet system for common letters
Morse_Alphabet = ["*Nun*", "a", " .- ", "b", " -... ", "c", " -.-. ", "d", " -.. ", "e", " . ", "f",\
" ..-. ", "g", " --. ", "h", " .... ", "i", " .. ", "j", " .--- ", "k", " -.- ", "l", " .-.. ",\
"m", " -- ", "n", " -. ", "o", " --- ", "p", " .--. ", "q", " --.- ", "r", " .-. ", "s", " ... ", "t",\
" - ", "u", " ..- ", "v", " ...- ", "w", " .-- ", "x", " -..- ", "y", " -.-- ", "z", " --.. "]

# Morse-code alphabet system for capital letters
Morse_Alphabet0 = ["*Nun*", "A", " .- ", "B", " -... ", "C", " -.-. ", "D", " -.. ", "E", " . ", "F",\
" ..-. ", "G", " --. ", "H", " .... ", "I", " .. ", "J", " .--- ", "K", " -.- ", "L", " .-.. ", "M",\
" -- ", "N", " -. ", "O", " --- ", "P", " .--. ", "Q", " --.- ", "R", " .-. ", "S", " ... ", "T",\
" - ", "U", " ..- ", "V", " ...- ", "W", " .-- ", "X", " -..- ", "Y", " -.-- ", "Z", " --.. "]

# Number system in morse code
Morse_Numeric = ["Nil!8*", "1", " .---- ", "2", " ..--- ", "3", " ...-- ", "4", " ....- ", "5",\
" ..... ", "6", "-.... ", "7", " --... ", "8", " ---.. ", "9", " ----. ", "0", "----- "]

# Dictionary alteration-check(OPTIONAL USE)
def alter_Check():
    if ( len( Morse_Alphabet ) - 1) == 52:
        print("\nAlphabet unaltered, alphabet count: " + str(len(Morse_Alphabet)-1))
    #
    if (len(Morse_Numeric) - 1) == 10:
        print("\nNumerics unaltered, number count: " + str(len(Morse_Numeric)-1) + "\n")
    else:
        print("\n\nDictionaries seem altered, check if you made any changes accidentally.\n")

nameEntry0 = input("\nHello there user, would you like to enter your name? (y or n): ")
user_Name0 = " "

# Name entry (OPTIONAL remove possibly)
if (nameEntry0 == "y" or nameEntry0 == "Y"):
    user_Name0 = input("\nOk thank you what is your name?: ")
    print("\n\nHello there " + user_Name0 + ", my name is Tammy the morse code Translator! 😄\n")
# In case the user doesn't want to enter their name
elif (nameEntry0 == "N" or nameEntry0 == "n"):
    user_Name0 = "User"
    print("\nWell thats a shame! i'll just have to call you " + user_Name0 + "!\n\nMy name is Tammy the morse translator!")
# Exception if the user doesnt enter correctly
else:
    print("BZZZ! Sorry I didn't understand that! Type correctly or I'll blow a fuse! (literally)😳")
    user_Name0 = "User"
# End of name entry

# Gets the user's message to be translated
message0 = input("\n\nThis bot translates morse code! which you might have figured out by now!\n\nWhat would you like to translate?: ")
counter0 = 0

# Spacing for morse code
dash_Bar = "/"
Morse_array0 = []

# TRANSLATES WORDS TO MORSE CODE \/\/\/          \/\/
def translator_Morse():
    counter0 = 0
    while counter0 < len(message0):
        if (message0[counter0] == " "):
            Morse_array0.extend(dash_Bar)
    # SPACEBAR ABOVE /\/\/\/\/\/\/\//\/\/\
        if (message0[counter0] == Morse_Alphabet[1]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[2])
        #
        if (message0[counter0] == Morse_Alphabet[3]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[4])
        ##
        if (message0[counter0] == Morse_Alphabet[5]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[6])
        #
        if (message0[counter0] == Morse_Alphabet[7]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[8])
        ##
        if (message0[counter0] == Morse_Alphabet[9]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[10])
        #
        if (message0[counter0] == Morse_Alphabet[11]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[12])
        ##
        if (message0[counter0] == Morse_Alphabet[13]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[14])
        #
        if (message0[counter0] == Morse_Alphabet[15]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[16])

        if (message0[counter0] == Morse_Alphabet[17]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[18])
        #
        if (message0[counter0] == Morse_Alphabet[19]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[20])

        if (message0[counter0] == Morse_Alphabet[21]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[22])
        #
        if (message0[counter0] == Morse_Alphabet[23]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[24])

        if (message0[counter0] == Morse_Alphabet[25]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[26])
        #
        if (message0[counter0] == Morse_Alphabet[27]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[28])

        if (message0[counter0] == Morse_Alphabet[29]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[30])

        if (message0[counter0] == Morse_Alphabet[31]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[32])

        if (message0[counter0] == Morse_Alphabet[33]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[34])

        if (message0[counter0] == Morse_Alphabet[35]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[36])

        if (message0[counter0] == Morse_Alphabet[37]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[38])

        if (message0[counter0] == Morse_Alphabet[39]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[40])

        if (message0[counter0] == Morse_Alphabet[41]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[42])

        if (message0[counter0] == Morse_Alphabet[43]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[4])

        if (message0[counter0] == Morse_Alphabet[45]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[46])

        if (message0[counter0] == Morse_Alphabet[47]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[48])

        if (message0[counter0] == Morse_Alphabet[49]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[50])

        if (message0[counter0] == Morse_Alphabet[51]) and (message0[counter0].islower):
            Morse_array0.extend(Morse_Alphabet[52])

        # UPPERCASE EXCEPTIONS

        if (message0[counter0] == Morse_Alphabet0[1]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[2])
        #
        if (message0[counter0] == Morse_Alphabet0[3]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[4])
        ##
        if (message0[counter0] == Morse_Alphabet0[5]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[6])
        #
        if (message0[counter0] == Morse_Alphabet0[7]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[8])
        ##
        if (message0[counter0] == Morse_Alphabet0[9]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[10])
        #
        if (message0[counter0] == Morse_Alphabet0[11]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[12])
        #
        if (message0[counter0] == Morse_Alphabet0[13]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[14])
        #
        if (message0[counter0] == Morse_Alphabet0[15]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[16])

        if (message0[counter0] == Morse_Alphabet0[17]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[18])
        #
        if (message0[counter0] == Morse_Alphabet0[19]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[20])

        if (message0[counter0] == Morse_Alphabet0[21]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[22])
        #
        if (message0[counter0] == Morse_Alphabet0[23]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[24])

        if (message0[counter0] == Morse_Alphabet0[25]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[26])
        #
        if (message0[counter0] == Morse_Alphabet0[27]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[28])

        if (message0[counter0] == Morse_Alphabet0[29]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[30])

        if (message0[counter0] == Morse_Alphabet0[31]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[32])

        if (message0[counter0] == Morse_Alphabet0[33]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[34])

        if (message0[counter0] == Morse_Alphabet0[35]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[36])

        if (message0[counter0] == Morse_Alphabet0[37]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[38])

        if (message0[counter0] == Morse_Alphabet0[39]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[40])

        if (message0[counter0] == Morse_Alphabet0[41]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[42])

        if (message0[counter0] == Morse_Alphabet0[43]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[4])

        if (message0[counter0] == Morse_Alphabet0[45]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[46])

        if (message0[counter0] == Morse_Alphabet0[47]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[48])

        if (message0[counter0] == Morse_Alphabet0[49]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[50])

        if (message0[counter0] == Morse_Alphabet0[51]) and (message0[counter0].isupper):
            Morse_array0.extend(Morse_Alphabet[52])

    # NUMBERS HANDLING
        if (message0[counter0] == Morse_Numeric[1]):
            Morse_array0.extend(Morse_Alphabet[2])

        if (message0[counter0] == Morse_Numeric[3]):
            Morse_array0.extend(Morse_Alphabet[4])

        if (message0[counter0] == Morse_Numeric[5]):
            Morse_array0.extend(Morse_Alphabet[6])

        if (message0[counter0] == Morse_Numeric[7]):
            Morse_array0.extend(Morse_Alphabet[8])

        if (message0[counter0] == Morse_Numeric[9]):
            Morse_array0.extend(Morse_Alphabet[10])

        if (message0[counter0] == Morse_Numeric[11]):
            Morse_array0.extend(Morse_Alphabet[12])

        if (message0[counter0] == Morse_Numeric[13]):
            Morse_array0.extend(Morse_Alphabet[14])

        if (message0[counter0] == Morse_Numeric[15]):
            Morse_array0.extend(Morse_Alphabet[16])

        if (message0[counter0] == Morse_Numeric[17]):
            Morse_array0.extend(Morse_Alphabet[18])

        if (message0[counter0] == Morse_Numeric[19]):
            Morse_array0.extend(Morse_Alphabet[20])

    #very crucial below
        counter0 += 1
#end of translations 

# first

translator_Morse()
# System messages after translation
print("\n\n\nHere is your translation!: \n")
print("".join(Morse_array0))
print("\n\nOriginal message: " + message0 + "\n")

# Saves logs of your morse translations for later use in the same place as the .py file
# Set 'a' to 'w' if you want to erase previous translations (OPTIONAL)
with open('MorseCodeTranslations_Logs.txt', 'a', encoding="utf-8") as f:
    f.write("__________________________________________________________\n\n" + "Here is your translation " + user_Name0 + "! :\n\n")
    f.write(''.join(Morse_array0))
    f.write("\n\nPrevious message entered: \n" + message0 + "\n\n")
    #
    current0 = datetime.now()
    currTime = current0.strftime("%H:%M:%S")
    f.write("\n__________________________________________________________\n\n\n" + 'Follow me on github, https://github.com/Hoccyy thank you! | \n\n__________________________________________________________ \n \
    \nTime : ' + currTime + "                                          |\n\n__________________________________________________________\n\n\n#\n\n")
# Opens my Github, Follow me by the way https://github.com/Hoccyy :) 
link0 = 'https://github.com/Hoccyy'
wb.open(link0)