s = input("Enter a string: ")
l = len(s)
s1 = ""
s2 = ""
i = 0
while i<l:
    if i%2==0:
        s1 += s[i]
    else:
        s2 += s[i]
    i += 1    
print("character at even position: ",s1)
print("character at odd position: ",s2) 

s = input("Enter a string: ")
odd_pos_char = s[1::2]
even_pos_char = s[0::2]
print("character at even position: ",odd_pos_char)
print("character at odd position: ",even_pos_char)     


