def get_pal_words(words):
    
    pal_w = []
    
    for word in words:
        
        if word == word[::-1]:
            pal_w.append(word)
    
    return pal_w        

def get_long_words(words):
    
    long_w = []
    
    for word in words:
        
        if len(word) >= 5:
            long_w.append(word)
            
    return long_w
    
def get_short_words(words):
    
    short_w = []
    
    for word in words:
        
        if len(word) <= 3:
            short_w.append(word)
    
    return short_w        

text = "анна арбуз дом шалаш кот окно аза"

words = text.split()

pal_words = get_pal_words(words)
long_words = get_long_words(words)
short_words = get_short_words(words)

print(f"Палиндромы: {pal_words}")

print(f"Длинные слова: {long_words}")

print(f"Короткие слова: {short_words}")
