def RomanToInt(roman_input):
    roman={"M":1000,"D":500,"C":100,"X":10,"L":50,"V":5,"I":1}
    result=0
    for i in range(0,len(roman_input)-1):
        if roman[roman_input[i]]<roman[roman_input[i+1]]:
            result-=roman[roman_input[i]]
        else:
            result+=roman[roman_input[i]]
    return result+roman[roman_input[-1]]
roman_input=input("Enter your Roman numeral: ")
print(RomanToInt(roman_input))