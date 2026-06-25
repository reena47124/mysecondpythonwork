#practice
sentence = "apple banana apple mango banana apple"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)