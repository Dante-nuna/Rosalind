#TREE2

n = 10
adjacent = [['1', '2'], ['2', '8'], ['4', '10'], ['5', '9'], ['6','10'], ['7', '9']]

def merge(s1, s2, pair):
    if pair[0] in s1 and pair[1] in s2:
        s1.extend(s2)
    return s1
'''
group = [adjacent[0]]
for pair in adjacent:
    for subgroup in group:
        a = 0
        b = 0
        if pair[0] in subgroup:
            for subgroup2 in group:
                if pair[1] in subgroup2:
                    group.append(subgroup.extend(subgroup2))
                    group.remove(subgroup2)
                    a += 1
            if a == 0:
                subgroup.append(pair[1])
                a += 1
        elif pair[1] in subgroup:
            for subgroup1 in group:
                if pair[0] in subgroup1:
                    group.append(subgroup.extend(subgroup1))
                    group.remove(subgroup1)
                    b += 1
            if b == 0:
                subgroup.append(pair[0])
                b += 1
    
        if a == 0 and b == 0:
            group.append(pair)
print(group)
'''
group = []
while len(adjacent) > 0:
    pair = adjacent[0]
    a = 0
    for subgroup in group:
        if pair[0] in subgroup:
            subgroup.append(pair[1])
            adjacent.remove(pair)
            a += 1
            break
            
        if pair[1] in subgroup:
            subgroup.append(pair[0])
            adjacent.remove(pair)
            a += 1
            break
    if a == 0:
        group.append(pair)
        adjacent.remove(pair)

print(group)