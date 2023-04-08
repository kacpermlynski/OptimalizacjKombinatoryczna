import random
import numpy as np
import time


def create_randomize_graph(n:int) -> list:
    matrix = np.zeros((n,n))
    for row in range(n):
        for element_row in range(n):
            value = np.random.rand()
            if value < 0.5:
                matrix[row][element_row] = 1
                matrix[element_row][row] = 1
    return matrix

def count_triangles_by_multipication(matrix:list):
    A = np.matrix(matrix )
    A_squared = A @ A
    T = A_squared @ A
    n = T.shape[0]
    num_triangles = np.trace(T) / 6
    return num_triangles

def count_triangles_by_naive_method(matrix:list):
    counter = 0
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            for k in range(j+1, len(matrix)):
                if matrix[i][j] and matrix[j][k] and matrix[k][i]:
                    counter += 1
    return counter

def count_traingle_by_dfs_method(matrix:list)->int:
    n = len(matrix)
    count = 0
    for i in range(n):
        visited = [False] * n
        stack = [i]
        while stack:
            v = stack.pop()
            visited[v] = True
            for j in range(n):
                if matrix[v][j] and not visited[j]:
                    for k in range(n):
                        if matrix[j][k] and matrix[k][v]:
                            count += 1
            stack.extend([j for j in range(n) if matrix[v][j] and not visited[j]])

    return count // 6 

def experimente(count_of_tries:int):
    list_of_matrix = []
    for x in range(count_of_tries):
        random_size = random.randrange(1,50)
        matrix = create_randomize_graph(random_size)
        list_of_matrix.append(matrix)
    

    results = {
        "NativeMethod":[],
        "DFSMethod":[],
        "MultipleMethod":[]
    }

    for matrix in list_of_matrix:
        startTime = time.time()
        counter = count_triangles_by_naive_method(matrix)
        results["NativeMethod"].append([counter,time.time()-startTime])
        startTime = time.time()
        counter = count_traingle_by_dfs_method(matrix)
        results["DFSMethod"].append([counter,time.time()-startTime])
        startTime = time.time()
        counter = count_triangles_by_multipication(matrix)
        results["MultipleMethod"].append([counter,time.time()-startTime])

    return results

if __name__ == "__main__":
    number_Of_experiments = int(input(""))
    results = experimente(number_Of_experiments)
    print(results)