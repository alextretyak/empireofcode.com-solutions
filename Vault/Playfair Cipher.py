def gen_key_table(key):
    t = []
    for c in key + "abcdefghijklmnopqrstuvwxyz0123456789":
        if c not in t:
            t.append(c)
    return t
    r = []
    for y in range(6):
        row = []
        for x in range(6):
            row.append(t[y*6+x])
        r.append(row)
    return r
    
def get_pos(c, table):
    i = table.index(c)
    return i%6, i//6
    
import re

def encode(message, key):
    message = re.sub('[^a-z0-9]', '', message.lower())
    i = 0
    while i < len(message):
        if i == len(message)-1:
            message = message[:i+1] + ('z' if message[i] != 'z' else 'x') + message[i+1:]
        elif message[i] == message[i+1]:
            message = message[:i+1] + ('x' if message[i] != 'x' else 'z') + message[i+1:]
        i += 2
        
    t = gen_key_table(key)
    r = ''
    for c1, c2 in zip(message[::2], message[1::2]):
        x1,y1 = get_pos(c1, t)
        x2,y2 = get_pos(c2, t)
        if y1 == y2:
            r += t[y1*6 + (x1+1)%6] + t[y2*6 + (x2+1)%6]
        elif x1 == x2:
            r += t[(y1+1)%6*6 + x1] + t[(y2+1)%6*6 + x2]
        else:
            r += t[y1*6 + x2] + t[y2*6 + x1]
    
    return r


def decode(message, key):
    t = gen_key_table(key)
    r = ''
    for c1, c2 in zip(message[::2], message[1::2]):
        x1,y1 = get_pos(c1, t)
        x2,y2 = get_pos(c2, t)
        if y1 == y2:
            r += t[y1*6 + (x1+5)%6] + t[y2*6 + (x2+5)%6]
        elif x1 == x2:
            r += t[(y1+5)%6*6 + x1] + t[(y2+5)%6*6 + x2]
        else:
            r += t[y1*6 + x2] + t[y2*6 + x1]
    
    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
