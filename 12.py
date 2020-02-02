import copy

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        connections = []

        for ix1, i in enumerate(M):
            for ix2, j in enumerate(i):
                if j == 1:
                    connections.append([ix1, ix2])

        # print(connections)

        connections_dict = dict()
        # for student_ix in set([j for i in connections for j in i]):
        #     print(student_ix)

        for student_ix in range(len(M)):
            connections_dict[student_ix] = []
            for item in connections:
                if item[0] == student_ix:
                    connections_dict[student_ix].append(item[1])
                elif item[1] == student_ix:
                    connections_dict[student_ix].append(item[0])
            connections_dict[student_ix] = list(set(connections_dict[student_ix]))

        networks = []

        # create networks
        for k, v in connections_dict.items():
            temp_networks = []
            for k2, v2 in connections_dict.items():
                temp_networks.append([x for x in v if k in v2])
            networks.append(temp_networks)

        flattened_networks = []
        for item in networks:
            flattened_networks.append(list(set([i for j in item for i in j])))

        copy_flattened_networks = copy.deepcopy(flattened_networks)
        new_flattened_networks = []
        ix = 0

        network_len = len(copy_flattened_networks) - 1

        while ix < network_len:
            for student in copy_flattened_networks[ix]:
                # for student2 in copy_flattened_networks[ix + 1]:
                if student in copy_flattened_networks[ix + 1]:
                    for x in copy_flattened_networks[ix + 1]:
                        copy_flattened_networks[ix].append(x)
                    copy_flattened_networks.remove(copy_flattened_networks[ix + 1])
                    copy_flattened_networks[ix] = list(set(copy_flattened_networks[ix]))
                    network_len = len(copy_flattened_networks) - 1
                    break
            ix += 1


        final_set = []
        print(copy_flattened_networks)
        for x in copy_flattened_networks:
            string_network = ""
            for y in x:
                string_network += str(y)
            final_set.append(string_network)

        final_set = list(set(final_set))

        return len(final_set)


s = Solution()
print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))