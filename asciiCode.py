#Name: Amaris Efthimiou
#Email: Amaris.Efthimiou66@myhunter.cuny.edu
#Date: September 17th, 2019
#Program: Ascii Code

word=input("type in something here: ")
codedWord=""
for ch in word:
    offset=ord(ch)-ord('a') + 13
    wrap= offset % 26
    newChar= chr(ord('a') + wrap)
    codedWord = codedWord + newChar
print(codedWord)

