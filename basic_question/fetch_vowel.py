def fetch_vowel(s:str)->None:

      for ch in str:
         if ch in "aeiouAEIOU":
            print(ch,end=" ")

str = input("Enter the string:")

fetch_vowel(str)