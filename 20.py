import collections


def criticalConnection(numOfServers, numOfConnections, connections):
    # WRITE YOUR CODE HERE

    connections_dict = {}

    low = [0] * numOfServers

    connections_dict = collections.defaultdict(list)

    for a, b in connections:
        connections_dict[a].append(b)
        connections_dict[b].append(a)

    print(connections_dict)

    def get_node_rank(rank, current, parent):

        low[current] = rank
        output = []

        for node in connections_dict[current]:
            if node == parent:
                continue
            if low[node] == 0:
                output += get_node_rank(rank + 1, node, current)
            low[current] = min(low[current], low[node])

            print(low[current])

            if low[node] > rank:
                output.append([node, current])
        return [connections[x] for x in output]

    get_node_rank(1, 0, -1)


print(criticalConnection(6,5, [[1,2], [2,3],[3,4], [4,5],[6,3]]))