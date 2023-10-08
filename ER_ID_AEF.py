AEF_ID = {
    "Alphabet" : ["_"] + [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)] + [chr(i) for i in range(ord('0'), ord('9')+1)] ,
    "states" : ["e0", "e1"],
    "Fstates" : ["e1"],
    "Istate" : "e0",
    "Transition" : {
        "e0" : {
            "a" : "e1", "b" : "e1", "c" : "e1", "d" : "e1", "e" : "e1", "f" : "e1",
            "g" : "e1", "h" : "e1", "i" : "e1", "j" : "e1", "k" : "e1", "l" : "e1",
            "m" : "e1", "n" : "e1", "o" : "e1", "p" : "e1", "q" : "e1", "r" : "e1",
            "s" : "e1", "t" : "e1", "u" : "e1", "v" : "e1", "w" : "e1", "x" : "e1",
            "y" : "e1", "z" : "e1", "A" : "e1", "B" : "e1", "C" : "e1", "D" : "e1",
            "E" : "e1", "F" : "e1", "G" : "e1", "H" : "e1", "I" : "e1", "J" : "e1",
            "K" : "e1", "L" : "e1", "M" : "e1", "N" : "e1", "O" : "e1", "P" : "e1",
            "Q" : "e1", "R" : "e1", "S" : "e1", "T" : "e1", "U" : "e1", "V" : "e1",
            "W" : "e1", "X" : "e1", "Y" : "e1", "Z" : "e1", "_" : "e1"
        },
        "e1" : {
            "a" : "e1", "b" : "e1", "c" : "e1", "d" : "e1", "e" : "e1", "f" : "e1",
            "g" : "e1", "h" : "e1", "i" : "e1", "j" : "e1", "k" : "e1", "l" : "e1",
            "m" : "e1", "n" : "e1", "o" : "e1", "p" : "e1", "q" : "e1", "r" : "e1",
            "s" : "e1", "t" : "e1", "u" : "e1", "v" : "e1", "w" : "e1", "x" : "e1",
            "y" : "e1", "z" : "e1", "A" : "e1", "B" : "e1", "C" : "e1", "D" : "e1",
            "E" : "e1", "F" : "e1", "G" : "e1", "H" : "e1", "I" : "e1", "J" : "e1",
            "K" : "e1", "L" : "e1", "M" : "e1", "N" : "e1", "O" : "e1", "P" : "e1",
            "Q" : "e1", "R" : "e1", "S" : "e1", "T" : "e1", "U" : "e1", "V" : "e1",
            "W" : "e1", "X" : "e1", "Y" : "e1", "Z" : "e1", "_" : "e1", "0" : "e1",
            "1" : "e1", "2" : "e1", "3" : "e1", "4" : "e1", "5" : "e1", "6" : "e1",
            "7" : "e1", "8" : "e1", "9" : "e1"
        }
    }
}
def simulation_AEF_ID(AEF, word):
    Cstate = AEF["Istate"]
    for char in word:
        if char not in AEF["Alphabet"] :
            print("Error, the char ", char, " doesn't exist.")
            return False
        if char not in AEF["Transition"][Cstate]:
            #print("Error, No transaction form ", Cstate, " with the char ", char)
            print("you can't start with the char ", char)
            return False
        Cstate = AEF["Transition"][Cstate][char]
    if Cstate in AEF["Fstates"]:
        return True
    else: return False

print("Welcome.\nThis application test if the ID of a variable is correct!\nWhat is your ID to check if it is available : ")
ID = input()
result = simulation_AEF_ID(AEF_ID, ID)
if result:
    print("The id is correct")
else: print("The id is not correct, make sure that he start's with a leter first or \"_\".")
