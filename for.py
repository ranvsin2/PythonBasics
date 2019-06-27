#range(start,stop,step)
#step:print every no after step.
for i in range(1,6,2):
    print(i)
fish=['rohu','katla','shark','mangur']
for f in fish:
    print(f)
for item in range(len(fish)):
    fish.append('jhinga')
    print(fish)
sammy='Mangur'
for letter in sammy:
    print (letter)
fish_dict={'name':'rohu','color':'brown','taste':'excellent','animal':'aqua'}
for key in fish_dict:
    print(key+"====="+fish_dict[key])