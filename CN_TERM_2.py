def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if (graph[vertex]) is not None:
                queue.extend(set(graph[vertex]) - visited)

    return visited

def checkNodeReachesDest(dictNodes, src,dst,values):
    results = []
    #print("Values: for first pass: ", values)
    for index in range(len(values)):
        new_source = values[index]
        visited = bfs(dictNodes,new_source)
        if len(visited)>1:
            if dst in visited:
                results.append(True)
            else:
                results.append(False)
        else:
            results.append(False)
        #print(visited, results)
    return results


def canWeMergePartial(dictNodes,result):
    count = 0
    for each in result:
        if each == True:
            count+=1
    if count>=2:
        return True
    return False


def canWeMergeEntire(dictNodes,result):
    #print("Reached here ...")
    #print(result)
    if False in result:
        return False
    return True

def mergeEntire(dictNodes, keys, keyToCheck):
    nodes_to_merge = dictNodes[keyToCheck]
    #dup_nodes_to_merge = nodes_to_merge[::]
    merged_nodes = ""
    merged_set = set()
    length = len(nodes_to_merge)
    #print(keys)
    while length!=0:
        temp_node = nodes_to_merge.pop()
        #print("Important",temp_node, keys)
        keys.remove(temp_node)
        merged_nodes+=temp_node
        length-=1
        #print(dictNodes)
        temp_list = dictNodes[temp_node]
        dictNodes.pop(temp_node)
        for each in temp_list:
            merged_set.add(each)
    dictNodes[merged_nodes] = [each for each in merged_set]
    dictNodes[keyToCheck].append(merged_nodes)
    keys.insert(0,merged_nodes)
    #print("Keys:: ", keys)

def mergePartial(dictNodes, keys, keyToCheck,result):
    nodes_to_merge = dictNodes[keyToCheck]
    dup_nodes_to_merge = nodes_to_merge[::]
    merged_nodes = ""
    merged_set = set()
    length = len(dup_nodes_to_merge)
    while length != 0:
        temp_result = result.pop()
        #print(temp_result)
        temp_popped = dup_nodes_to_merge.pop()
        length -= 1
        if temp_result is not False:

            temp_node = nodes_to_merge.pop(nodes_to_merge.index(temp_popped))
            keys.remove(temp_node)
            merged_nodes += temp_node
            temp_list = dictNodes[temp_node]
            dictNodes.pop(temp_node)
            for each in temp_list:
                merged_set.add(each)

    dictNodes[merged_nodes] = [each for each in merged_set]
    dictNodes[keyToCheck].append(merged_nodes)
    keys.insert(0,merged_nodes)
    #print(dictNodes)

def todo(dictNodes, src, dst):
    """
    Main Driver function
    :param dictNodes: The dict of the graph
    :param src: The Node to start with
    :param dst: The node we have to reach
    :return: A compressed graph which helps BGP run effectively
    """
    keys = list(dictNodes.keys())

    while len(keys)!=0:
        keyToCheck = keys[0]
        #print(keyToCheck)
        keys.remove(keyToCheck)
        values = dictNodes.get(keyToCheck)
        if values is not None and len(values)>1:
            result = checkNodeReachesDest(dictNodes,keyToCheck,dst, values)
            canMerge = canWeMergeEntire(dictNodes,result)
            if canMerge:
                mergeEntire(dictNodes,keys,keyToCheck)
            else:
                can_we_merge_partial = canWeMergePartial(dictNodes,result)
                if can_we_merge_partial:
                    mergePartial(dictNodes,keys,keyToCheck,result)

    print(dictNodes)




#dictNodes ={
 #   "A": ["B","C"], "B":['G'], "C":['H'], 'G':['D'], 'H':['E'] ,'E':['D'],'D':None
#}

dictNodes = {
	'A':['B','C'] , 'B':['D'], 'C':['E'], 'E':['D'], 'D':None
}
src = "A"
dst = "D"
todo(dictNodes,src,dst)
