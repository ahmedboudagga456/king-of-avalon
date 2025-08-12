import random
names=["ahmed","mohamed","ali"]

def create_display(word):
    display = ["_"] * len(word)
    print(''.join(display))
    print("\n".join(display))
    return display

random_name = random.choice(names)
10 | display = create_display(random_name)