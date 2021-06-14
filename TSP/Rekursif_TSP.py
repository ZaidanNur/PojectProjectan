from itertools import permutations
#1. Hitung harga antar titik pada setiap grafnya
list_warga_rt9 = ['TPA','tono',"AIS",'liptaa']
Graf_soal = [[0,3,2,4],
            [3,0,3,5],
            [2,3,0,2],
            [4,5,2,0]]

Starting_point = 0


def node(graf,sp,nodes=[],count=0): # 0 1 2 3 -> 1 2 3 / 1 3 2
    if count==len(graf):
        k = permutations(nodes) # Mencari permutasi path yang mungkin
        # ((1,2,3)(1,3,2)(2,3,1)...)
        all_nodes = []
        for i in k:
            all_nodes.append(i)
        return all_nodes
    elif count==sp:
        return node(graf,sp,nodes,count+1)
    else:
        nodes.append(count)
        return node(graf,sp,nodes,count+1)

def TSP(graf,startpoint,nodes=[],c_cost=0,count=0,all_cost=[]):
    if count == len(nodes):
        print(all_cost)
        min_cost = min(all_cost)
        location = [i for i, val in enumerate(all_cost) if val==min_cost]
        print(location)
        print("Path(s) with minimal cost :")
        for i in location:
            print(list_warga_rt9[0],end='->')
            for j in nodes[i]:
                print(list_warga_rt9[j],end='->')
            print(list_warga_rt9[0])
        return min_cost
    else:
        nodes_now= nodes[count] # (1,2,3) / (1, 3, 2)
        k = startpoint # 0
        for j in nodes_now:
            c_cost+= graf[k][j] # 0-> 1 / 1 -> 2/ 2 -> 3
            k=j #3
        c_cost+=graf[k][startpoint]
        all_cost.append(c_cost)
        return TSP(graf,startpoint,nodes,0,count=count+1,all_cost=all_cost)

print(node(Graf_soal,0,[],0))
print(f"Minimal cost : {TSP(graf=Graf_soal,startpoint=Starting_point,nodes=node(Graf_soal,0,[],0))}")