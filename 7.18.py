def function(sentence):
    new_sentence=""
    for i in sentence:
        if i!=" ":
            new_sentence+=i
    return new_sentence

print(function("integrated development environment"))
print(function("A programming language is a system of notation for writing computer programs"))