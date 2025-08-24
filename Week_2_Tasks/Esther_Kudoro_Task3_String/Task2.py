#TASK 2
#6) checking if a string contain the substring 'Python'
print("checking if a string contain the substring 'Python'")
text = "Contemplating including python in this or not, also python is case sensitive"
print("python" in text)

#7) Reversing a string
print("Reversing a string")
rgreet = reversed("Hello how are you doing?")
rev_greet = "".join(rgreet)
print(rev_greet)

#8) Removing extra spaces
print("Removing extra spaces")
text = " Hi, it's nice to finally meet you "
print(text.strip())

#9 print vowels
print("print vowels")
sent = input("Please enter a sentence: ").lower()
vowel_o = sent.count("o")
vowel_i = sent.count("i")
vowel_u = sent.count("u")
vowel_e = sent.count("e")
vowel_a = sent.count("a")
total = vowel_o + vowel_i + vowel_u + vowel_e + vowel_a
print(total)

#10 Converting string to int
print("Converting string to int")
string = "1234"
mult = int(string)
print(mult*2)
