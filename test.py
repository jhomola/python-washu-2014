sentence = "Hello world. How are you."
sentence = sentence.replace(".", "  .")
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print sentence_rev