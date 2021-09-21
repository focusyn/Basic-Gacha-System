import random

class WishItems:
    rarity = "None"
    def __init__(self, pity=0):
        if pity > 50:
            pityx = 11
        elif pity > 75:
            pityx = 22
        else:
            pityx = 1
        Characters = ["SSR Character", "Rare Character", "Uncommon Character", "Common Character"]
        l = Characters
        l +=["SSR Character"]*pityx
        l +=["Rare Character"]*5
        l +=["Uncommon Character"]*20
        l +=["Common Character"]*(75-pityx)
        self.rarity = random.choice(l)


file = open("C:/Users/Aarnick/Desktop/gacha/pulls.txt",'r')
pitycounter = int(file.read())
file.close()


currentpitycounter = 0

print("Simulating 10 Pull: \n")
wishes = []
for i in range(10):
    wishes.append(WishItems(pitycounter+currentpitycounter+1))
    if(wishes[i].rarity=="SSR Character"):
        currentpitycounter=0
        pitycounter=0
    else:
        currentpitycounter+=1
for wish in wishes:
    print(wish.rarity)

file = open("C:/Users/Aarnick/Desktop/gacha/pulls.txt", 'w')
pitycounter+=currentpitycounter
file.write(str(pitycounter))
file.close()

print(f'\nPity: {pitycounter}')
