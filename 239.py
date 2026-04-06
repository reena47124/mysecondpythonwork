#string.
#count the number of vowels and consonants in a string.
s=input("enter a string:").lower()
vowel="aeiou"
v_count=0
c_count=0
for ch in s:
    if ch.isalpha():
        if ch in vowel:
            v_count+=1
        else:
            c_count+=1
print(f"number of vowels in the given string are:{v_count}")
print(f"number of consonants in the given string are:{c_count}")
