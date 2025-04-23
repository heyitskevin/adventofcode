def readfile():
    with open('input.txt') as f:
        return [int(x) for x in f.read().strip().split()]


def evaluate_graph(g):
    q = [g] 
    while q:
        next_node = q.pop(-1)
        if len(next_node['children']) == 0:
            next_node['value'] = sum(next_node['metadata'])
        elif all('value' in nn for nn in next_node['children']):
            val = 0
            for elem in next_node['metadata']:
                if 1 <= elem <= len(next_node['children']):
                    val += next_node['children'][elem - 1]['value']
            next_node['value'] = val
        else:
            q.append(next_node) # add it back if children haven't been eval'ed
            for c in next_node['children']:
                if 'value' not in c:
                    q.append(c)
    return g['value']

# Going to try and build a graph structure of the entire tree here for fun
# Depth first traversal
def main():
    data = readfile()
    def traverse(data_string, n_id):
        g = {'id': n_id, 'children': []}
        child_node_count, metadata_count = data_string[0], data_string[1]
        remaining_data = data_string[2:]
        if child_node_count == 0:
            return {'metadata': remaining_data[:metadata_count], 'children': [], 'id': n_id}, remaining_data[metadata_count:]
        for c in range(child_node_count):
            n_id += 1
            child_data, m = traverse(remaining_data, n_id)
            g['children'].append(child_data)
            remaining_data = m
        g['metadata'] = remaining_data[:metadata_count]
        
        return g, remaining_data[metadata_count:]
    
    graph, _ = traverse(data, 0)
    return evaluate_graph(graph)
    
print(main())