# Submit this file to Gradescope
from typing import List
# you may use other Python standard libraries, but not data
# science libraries, such as numpy, scikit-learn, etc.

def dist(a: List[float], b: List[float]):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

def replace_list_elements(l: list, before, after):
   return [(after if (e == before) else e) for e in l]

def reindex_clusters(clusters):
    unique_clusters = set(sorted(clusters))
    normalized_clusters = set([i for i in range(len(set(clusters)))])
    before_clusters = unique_clusters.difference(normalized_clusters)
    after_clusters = normalized_clusters.difference(unique_clusters)

    for b, a in zip(before_clusters, after_clusters):
        clusters = replace_list_elements(clusters, b, a)
    return clusters

class Solution:
  def hclus_single_link(self, X: List[List[float]], K: int) -> List[int]:
    """Single link hierarchical clustering
    Args:
      - X: 2D input data
      - K: the number of output clusters
    Returns:
      A list of integers (range from 0 to K - 1) that represent class labels.
      The number does not matter as long as the clusters are correct.
      For example: [0, 0, 1] is treated the same as [1, 1, 0]"""
    # implement this function

    N = len(X)
    dist_matrix = List[List[float]]
    dist_matrix = [[dist(X[i], X[j]) for i in range(N)] for j in range(N)]

    # Initialize clusters
    clusters = List[int]
    clusters = [i for i in range(N)]

    while len(set(clusters)) > K:
        # Calculate the minimum distance
        min_dist = float('inf')
        for i in range(N):
            for j in range(N):
                if clusters[i] == clusters[j]:
                    continue
                if (dist_matrix[i][j] <= min_dist) and (dist_matrix[i][j] != 0):
                    min_dist = dist_matrix[i][j]
                    min_dist_a = i
                    min_dist_b = j

        #clusters[min_dist_a] = clusters[min_dist_b]
        clusters = replace_list_elements(clusters, clusters[min_dist_b], clusters[min_dist_a])
        clusters = reindex_clusters(clusters)
        #print(min_dist_a, min_dist_b, min_dist)
        #print(clusters, len(set(clusters)))
    return clusters
  
  def hclus_average_link(self, X: List[List[float]], K: int) -> List[int]:
    """Complete link hierarchical clustering"""
    # implement this function
    pass

  def hclus_complete_link(self, X: List[List[float]], K: int) -> List[int]:
    """Average link hierarchical clustering"""
    # implement this function
    pass
