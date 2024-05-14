#a
print((NY['QS']))
print(NY.get("QS"))
#b
print(NY.get("LI", "Not in"))
print(NY.get('SI', 'absent'))
print(NY.setdefault('SI', 0.48))
#c
print("LI" in NY)
print('MN' not in NY)
#d
print(len(NY), min(NY), max(NY))
print(len(NY.items()),
max(NY.keys()), min(NY.values()))
#E
print(round(NY['QS']))
NY['QS'] += .3
print(round(NY['QS'], 1))
#F
print(NY.keys())
print(list(NY.values()))
print(tuple(NY.items()))
#G
total = 0
for x in NY.values():
 total += x
print(f'{total:.1f}')
#H
total = 0
for x in NY:
 total += NY[x]
print(f'{total:.1f}')
#I
for x in sorted(NY) : print(x, end = '|')
# j
NY = {"BX":1.42, "MN":1.63, "QS":2.25, "BN":2.56, "SI": 0.47}
for x in sorted(NY, reverse=True):
    print (x, end= '|')
print()
#K
for values in sorted(NY.values(), reverse=True):
    print (values, end= '|')
#l
if "QS" in NY: print("Queens is the most diverse county in NY.")

#m
for x, y in NY.items():
 if y > 2.5: print(f"{x} is the Kings county!")
#n
 NY["SK"] = 1.49
print(NY)
#o
NY.update({"NU":1.34})
print(NY)
#p
NY.pop("QS")
NY.popitem()
print(NY)
#Q
newYork = NY
del newYork['BN']
print(NY)
print(newYork)
#R
newYork = dict(NY)
del newYork["BN"]
print(len(NY))
print(len(newYork))
#S
NewYork = NY.copy()
NY.clear()
print(NY)
print(NewYork)
del NY
print(set(NewYork))    
