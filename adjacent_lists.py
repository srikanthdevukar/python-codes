edge_list=[('A','B',2),('B','D',4),('D','E',5),('C','E',1),('C','D',6),('A','C',3)]
tot=0
for edge in edge_list:
    tot+=edge[2]
print("total distance =",tot)
v_set=set()
for edge in edge_list:
    v_set.add(edge[0])
    v_set.add(edge[1])
no_of_nodes=len(v_set)
adj_list={v:[] for v in v_set}
for edge in edge_list:
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])
print("adj list:",adj_list)
