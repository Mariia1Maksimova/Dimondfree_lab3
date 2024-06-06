# -*- coding: utf-8 -*-

d_versh = {}
d_rebra = {}

count = 1
len_name = input('Кол-во вершин: ')
with open(f'Taxicab_{len_name}.txt', 'r') as file:
    file = file.readlines()[1:]
    for line in file:
        value = line.split()
        d_versh[count] = value
        count += 1
list_key = []
for key_i, value_i in d_versh.items():
    list_key.append(key_i)
    for key_j, value_j in d_versh.items():
        if key_i != key_j and key_j not in list_key:
            d_rebra[(key_i, key_j)] = (abs(int(value_i[0]) - int(value_j[0]))) + (
                abs(int(value_i[1]) - int(value_j[1])))

l = []

for key_i, value_i in d_rebra.items():
    l.append(key_i)

nodes_count = {}
for key_i, value_i in d_rebra.items():

    if key_i[0] not in nodes_count:
        nodes_count[key_i[0]] = 0
    if key_i[1] not in nodes_count:
        nodes_count[key_i[1]] = 0

    nodes_count[key_i[0]] += value_i
    nodes_count[key_i[1]] += value_i

pre_sorted_list = list(dict(sorted(nodes_count.items(), key=lambda item: item[1])).keys())


def create_bipartite_graph(l1, l2):
    edges = []
    for i in l1:
        for j in l2:
            if (i, j) or ((j, i) in l):
                edges.append((i, j))
            else:
                return False
    return edges


val = 0
j = int(input('Деление на группы: '))

pre_sorted_list2 = list(dict(sorted(nodes_count.items(), key=lambda item: item[0])).keys())
l1_li = pre_sorted_list2[j:]
l2_li = pre_sorted_list2[:j]


edges = create_bipartite_graph(l1_li, l2_li)

for item in edges:
    if item in d_rebra:
        val = val + d_rebra[item]
    elif (item[1], item[0]) in d_rebra:
        val = val + d_rebra[(item[1], item[0])]
print('score', val)

with open(f"Maksimova_{len_name}.txt", "w") as file:
    file.write(f"c Вес дерева = {val}, " + '\n')
    file.write(f"p edge {len_name} {len(edges)}" + '\n')
    for line in sorted(edges):
        file.write(f"e {line[0]} {line[1]}" + '\n')
