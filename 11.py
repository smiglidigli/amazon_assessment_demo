from collections import Counter


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """

        # [item for sublist in l for item in sublist]
        nodes = [x for y in connections for x in y]
        print(nodes)
        count_of_servers = Counter(nodes)
        print(count_of_servers)

        output = []

        unique_nodes = []

        for k, v in count_of_servers.items():
            if v % 2 != 0:
                unique_nodes.append(k)

        if len(unique_nodes) > 0:
            for item in unique_nodes:
                for connection in connections:
                    if item in connection:
                        if count_of_servers[connection[0]] % 2 != 0 and \
                            count_of_servers[connection[1]] % 2 != 0:
                            output.append(connection)

        return list(set(tuple(sorted(sub)) for sub in output))


s = Solution()
print(s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))