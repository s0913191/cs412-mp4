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

def get_list_index(l: list, e):
   return [i for i, x in enumerate(l) if x == e]

def cluster_min_distance(cluster_dist_matrix):
  # Calculate the minimum distance between clusters
  min_dist = float('inf')
  for i in range(len(cluster_dist_matrix)):
    for j in range(len(cluster_dist_matrix)):
      if i == j:
        continue
      if (cluster_dist_matrix[i][j] <= min_dist) and (cluster_dist_matrix[i][j] != 0):
        min_dist = cluster_dist_matrix[i][j]
        min_dist_a = i
        min_dist_b = j
  return min_dist, min_dist_a, min_dist_b

def single_link_distance(cluster1_index, cluster2_index, dist_matrix):
  """
  Args:
    - cluster1_index: 
    - cluster2_index:
    - dist_matrix: distance matrix for all input data points
  Returns:
    Min distance between clusters
  """
  min_dist = float('inf')
  for ci1 in cluster1_index:
      for ci2 in cluster2_index:
         if (dist_matrix[ci1][ci2] <= min_dist) and (dist_matrix[ci1][ci2] != 0):
            min_dist = dist_matrix[ci1][ci2]
  return min_dist

def complete_link_distance(cluster1_index, cluster2_index, dist_matrix):
  """
  Args:
    - cluster1_index: 
    - cluster2_index:
    - dist_matrix: distance matrix for all input data points
  Returns:
    Max distance between clusters
  """
  max_dist = -float('inf')
  for ci1 in cluster1_index:
      for ci2 in cluster2_index:
         if (dist_matrix[ci1][ci2] >= max_dist) and (dist_matrix[ci1][ci2] != 0):
            max_dist = dist_matrix[ci1][ci2]
  return max_dist


def average_link_distance(cluster1_index, cluster2_index, dist_matrix):
  """
  Args:
    - cluster1_index: 
    - cluster2_index:
    - dist_matrix: distance matrix for all input data points
  Returns:
    Average distance between clusters
  """
  avg_dist = 0

  for ci1 in cluster1_index:
      for ci2 in cluster2_index:
         avg_dist += dist_matrix[ci1][ci2]


  avg_dist /= len(cluster1_index)*len(cluster2_index)
  return avg_dist

"""
def average_link_distance(cluster1_index, cluster2_index, X):
  cluster1_sum_x = 0
  cluster1_sum_y = 0
  cluster2_sum_x = 0
  cluster2_sum_y = 0
  for ci1 in cluster1_index:
    cluster1_sum_x += X[ci1][0]
    cluster1_sum_y += X[ci1][1] 
    
  for ci2 in cluster2_index:
    cluster2_sum_x += X[ci2][0]
    cluster2_sum_y += X[ci2][1]

  x1 = cluster1_sum_x / len(cluster1_index)
  y1 = cluster1_sum_y / len(cluster1_index)
  x2 = cluster2_sum_x / len(cluster2_index)
  y2 = cluster2_sum_y / len(cluster2_index)

  distance = dist([x1, y1], [x2, y2])
  return distance
"""

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
    
    N = len(X)
    dist_matrix = List[List[float]]
    dist_matrix = [[dist(X[i], X[j]) for i in range(N)] for j in range(N)]

    # Initialize clusters
    clusters = List[int]
    clusters = [i for i in range(N)]
    num_of_clusters = len(set(clusters))

    while num_of_clusters > K:
      cluster_dist_matrix = List[List[float]]
      cluster_dist_matrix = [[0 for i in range(num_of_clusters)] for j in range(num_of_clusters)]

      for c1 in set(clusters):
         for c2 in set(clusters):
          if c1 == c2:
             continue
          cluster1_index = get_list_index(clusters, c1)
          cluster2_index = get_list_index(clusters, c2)
          cluster_dist_matrix[c1][c2] = single_link_distance(cluster1_index, cluster2_index, dist_matrix)

      min_dist, min_dist_a, min_dist_b = cluster_min_distance(cluster_dist_matrix)
      clusters = replace_list_elements(clusters, min_dist_b, min_dist_a)
      clusters = reindex_clusters(clusters)
      num_of_clusters = len(set(clusters))

    return clusters
  
  def hclus_average_link(self, X: List[List[float]], K: int) -> List[int]:
    """Average link hierarchical clustering"""
    N = len(X)
    dist_matrix = List[List[float]]
    dist_matrix = [[dist(X[i], X[j]) for i in range(N)] for j in range(N)]

    # not needed for average link
    #dist_matrix = List[List[float]]
    #dist_matrix = [[dist(X[i], X[j]) for i in range(N)] for j in range(N)]

    # Initialize clusters
    clusters = List[int]
    clusters = [i for i in range(N)]
    num_of_clusters = len(set(clusters))

    while num_of_clusters > K:
      cluster_dist_matrix = List[List[float]]
      cluster_dist_matrix = [[0 for i in range(num_of_clusters)] for j in range(num_of_clusters)]

      for c1 in set(clusters):
         for c2 in set(clusters):
          if c1 == c2:
             continue
          cluster1_index = get_list_index(clusters, c1)
          cluster2_index = get_list_index(clusters, c2)
          cluster_dist_matrix[c1][c2] = average_link_distance(cluster1_index, cluster2_index, dist_matrix)

      min_dist, min_dist_a, min_dist_b = cluster_min_distance(cluster_dist_matrix)
      clusters = replace_list_elements(clusters, min_dist_b, min_dist_a)
      clusters = reindex_clusters(clusters)
      num_of_clusters = len(set(clusters))
    return clusters

  def hclus_complete_link(self, X: List[List[float]], K: int) -> List[int]:
    """Complete link hierarchical clustering"""
    N = len(X)
    dist_matrix = List[List[float]]
    dist_matrix = [[dist(X[i], X[j]) for i in range(N)] for j in range(N)]

    # Initialize clusters
    clusters = List[int]
    clusters = [i for i in range(N)]
    num_of_clusters = len(set(clusters))

    while num_of_clusters > K:
      cluster_dist_matrix = List[List[float]]
      cluster_dist_matrix = [[0 for i in range(num_of_clusters)] for j in range(num_of_clusters)]

      for c1 in set(clusters):
         for c2 in set(clusters):
          if c1 == c2:
             continue
          cluster1_index = get_list_index(clusters, c1)
          cluster2_index = get_list_index(clusters, c2)
          cluster_dist_matrix[c1][c2] = complete_link_distance(cluster1_index, cluster2_index, dist_matrix)

      min_dist, min_dist_a, min_dist_b = cluster_min_distance(cluster_dist_matrix)
      clusters = replace_list_elements(clusters, min_dist_b, min_dist_a)
      clusters = reindex_clusters(clusters)
      num_of_clusters = len(set(clusters))

    return clusters
