#practice
sentence = "I love Python"
result = []
for word in sentence.split():
    result.append(word[::-1])
print(" ".join(result))