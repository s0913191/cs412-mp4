from submission import Solution
from typing import List

input_path = 'sample_test_cases/input00.txt'
output_path = 'sample_test_cases/output00.txt'

#input_path = 'sample_test_cases/test_input00.txt'
#output_path = 'sample_test_cases/test_output00.txt'

with open(input_path, 'r') as f:
    data = [tuple(float(e) for e in s.rstrip('\n').split(' ')) for s in f.readlines()]
    N = int(data[0][0])
    K = int(data[0][1])
    M = int(data[0][2])
    data = data[1:]

with open(output_path, 'r') as f:
    validate_clusters = [int(s.rstrip('\n')) for s in f.readlines()]


clustering = Solution()
clusters = clustering.hclus_single_link(data, K)
#clusters = clustering.hclus_complete_link(data, K)
#clusters = clustering.hclus_average_link(data, K)
#print('average link')


print(clusters, validate_clusters)





