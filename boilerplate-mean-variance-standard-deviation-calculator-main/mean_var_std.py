import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list, dtype=int)
    mat = arr.reshape(3, 3)

    calculations = {
        'mean': [mat.mean(axis=0).tolist(),
                 mat.mean(axis=1).tolist(),
                 mat.mean().tolist()],

        'variance': [mat.var(axis=0).tolist(),
                     mat.var(axis=1).tolist(),
                     mat.var().tolist()],

        'standard deviation': [mat.std(axis=0).tolist(),
                               mat.std(axis=1).tolist(),
                               mat.std().tolist()],

        'max': [mat.max(axis=0).tolist(),
                mat.max(axis=1).tolist(),
                mat.max().tolist()],

        'min': [mat.min(axis=0).tolist(),
                mat.min(axis=1).tolist(),
                mat.min().tolist()],

        'sum': [mat.sum(axis=0).tolist(),
                mat.sum(axis=1).tolist(),
                mat.sum().tolist()]
    }

    
    return calculations



if __name__ == "__main__":

    print(calculate([0,1,2,3,4,5,6,7,8]))