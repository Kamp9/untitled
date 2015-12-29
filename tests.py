import numpy as np
import scipy.linalg as sp
import lu
np.set_printoptions(linewidth=200)


def generate_pos_dif(n, fr, to):
    a = np.random.random_integers(fr, to, size=(n, n))
    b = np.random.random_integers(to * 10, to * 1000, size=(n, 1))
    pos_dif = (a + a.T)/2
    np.fill_diagonal(pos_dif, b)
    return pos_dif


"""
def row_substitution(U, B):
    m, n = U.shape
    r, n = B.shape
    U = U.astype(np.float64)
    B = B.astype(np.float64)
    x = np.zeros((r, n))
    for k in range(m):
        x[k] = (B[k] - np.dot(U[k, :k], x[:k])) / U[k, k]
    return x


def col_substitution(U, B):
    m, n = U.shape
    n, r = B.shape
    U = U.astype(np.float64)
    B = B.astype(np.float64)
    x = np.zeros((n, r))
    for k in range(m):
        x[:, k] = (B[:, k] - np.dot(x[:, :k], U[:k, k])) / U[k, k]
    return x


def lu_block(A, r):
    m, n = A.shape
    U = np.zeros((m, m))
    L = np.zeros((m, m))
    A = A.astype(np.float64)
    for k in range(0, m, r):
        decomp = lu.lu_inplace(A[k:k+r, k:k+r])
        L[k:k+r, k:k+r] = decomp[0]
        U[k:k+r, k:k+r] = decomp[1]
        L[k+r:, k:k+r] = col_substitution(U[k:k+r, k:k+r], A[k+r:, k:k+r])
        U[k:k+r, k+r:] = row_substitution(L[k:k+r, k:k+r], A[k:k+r, k+r:])
        A[k+r:, k+r:] -= np.dot(L[k+r:, k:k+r], U[k:k+r, k+r:])
    return L, U


def lu_out_of_place(A):
    A = A.astype(np.float64)
    m, n = A.shape
    if m > n:
        L = np.eye(m, n)
        U = np.zeros((n, n))
    else:
        L = np.eye(m, m)
        U = np.zeros((m, n))
    for k in range(min(m, n)):
        U[k, k:] = A[k, k:]
        L[k+1:, k] = A[k+1:, k] / U[k, k]
        A[k+1:, k+1:] -= L[k+1:, k, np.newaxis] * U[k, k+1:]
    return L, U
"""

rand_int_matrix = np.random.randint(-1000, 1000, size=(6, 6))

L, U = lu.lu_inplace(rand_int_matrix)
print L
print U
lu.row_substitution(L[:2, :2], rand_int_matrix[:2, 2:])