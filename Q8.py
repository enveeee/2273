sentence=input("Enter the sentence:")
words=sentence.split()
words.sort()
print(words)
print("The sentence after sorting the words:")
print(" ".join(words))
