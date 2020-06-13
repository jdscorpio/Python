letters = 'aeiou'

txt = input("Podaj tekst: ")
txt = txt.casefold()
count = {}.fromkeys(letters,0)

for ch in txt:
    if ch in count:
        count[ch] +=1

print(count)

