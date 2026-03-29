#Write a function that counts vowels in a string.
def func_vowel(s):
    count=0
    vowel="aeiouAEIOU"
    for ch in s:
        if ch in vowel:
            count+=1
    return count
print(func_vowel("hello there!"))        