# text = set(input("Enter some text: "))
# vowels = set(["a", "e", "i", "o", "u"])
text = "Python is a very powerful language"
vowels = frozenset("aeiou")

result = set(text).difference(vowels)
print(result)

print(sorted(result))
