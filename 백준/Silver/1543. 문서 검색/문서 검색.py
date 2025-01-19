def count_myfunc(document, word):
    count = 0
    start = 0

    while True:
        start = document.find(word, start)
        if start == -1:
            break
        count += 1
        start += len(word)
    
    return count

document = input()
word = input()

occurrences = count_myfunc(document, word)
print(occurrences)