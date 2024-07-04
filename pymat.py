import numpy as np

def mat4(initv):
    '''
    4 x 4 Matrix
    '''
    a=np.mat(np.eye(4,4))
    a=initv*a
    return a
def mat3(initv):
    '''
    3 x 3 Matrix
    '''
    a=np.mat(np.eye(3,3))
    a=initv*a
    return a
def tobytes(m):
    '''
    transform a matrix m to bytes
    '''
    a=m.A
    return a.tobytes()
def inverse(m):
    a=m.I
    return a