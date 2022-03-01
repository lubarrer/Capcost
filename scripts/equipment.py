import numpy as np


def range_sol(x, upper, lower):
    if x >= lower and x <= upper:
        X = x
        Y = 0
        return X, Y, upper
    elif x < lower:
        X = lower
        Y = 0
        return X, Y, upper
    elif x > upper:
        i = int(x / upper)
        if x % upper != 0:
            X = x - i * upper
            Y = i
            return X, Y, upper
        else:
            X = 0
            Y = i
            return X, Y, upper


def pump(W):
    x, y, z = range_sol(W, 300, 1)
    lpc = 4.1 + 0.06 * np.log10(z) + 0.18 * (np.log10(z)) ** 2
    pc = 10 ** lpc

    if x != 0:
        rlpc = 4.1 + 0.06 * np.log10(x) + 0.18 * (np.log10(x)) ** 2
        rpc = 10 ** rlpc
        fpc = y * pc + rpc
        return fpc
    else:
        fpc = y * pc
        return fpc


def heatex(A):
    x, y, z = range_sol(A, 1000, 20)
    lpc = 5.5 - 0.1 * np.log10(z) + 0.36 * (np.log10(z)) ** 2
    pc = 10 ** lpc

    if x != 0:
        rlpc = 5.5 - 0.1 * np.log10(x) + 0.36 * (np.log10(x)) ** 2
        rpc = 10 ** rlpc
        fpc = y * pc + rpc
        return fpc
    else:
        fpc = y * pc
        return fpc


def heater(Q):
    x, y, z = range_sol(Q, 100_000, 3000)
    lpc = 3.6 + 0.79 * np.log10(z) + 0.02 * (np.log10(z)) ** 2
    pc = 10 ** lpc

    if x != 0:
        rlpc = 3.6 + 0.79 * np.log10(x) + 0.02 * (np.log10(x)) ** 2
        rpc = 10 ** rlpc
        fpc = y * pc + rpc
        return fpc
    else:
        fpc = y * pc
        return fpc


def Vvessel(V):
    x, y, z = range_sol(V, 0.3, 520)
    lpc = 4.2 + 0.54 * np.log10(z) + 0.13 * (np.log10(z)) ** 2
    pc = 10 ** lpc

    if x != 0:
        rlpc = 4.2 + 0.54 * np.log10(x) + 0.13 * (np.log10(x)) ** 2
        rpc = 10 ** rlpc
        fpc = y * pc + rpc
        return fpc
    else:
        fpc = y * pc
        return fpc


def Hvessel(V):
    x, y, z = range_sol(V, 0.1, 628)
    lpc = 4.2 + 0.46 * np.log10(z) + 0.11 * (np.log10(z)) ** 2
    pc = 10 ** lpc

    if x != 0:
        rlpc = 4.2 + 0.46 * np.log10(x) + 0.11 * (np.log10(x)) ** 2
        rpc = 10 ** rlpc
        fpc = y * pc + rpc
        return fpc
    else:
        fpc = y * pc
        return fpc


def storageT(V):
    x, y, z = range_sol(V, 90, 30_000)
    lpc = 5.82 - 0.48 * np.log10(z) + 0.17 * (np.log10(z)) ** 2
    pc = 10 ** lpc

    if x != 0:
        rlpc = 5.82 - 0.48 * np.log10(x) + 0.17 * (np.log10(x)) ** 2
        rpc = 10 ** rlpc
        fpc = y * pc + rpc
        return fpc
    else:
        fpc = y * pc
        return fpc


__all__ = ["pump", "heatex", "heater", "Vvessel", "Hvessel", "storageT"]

classes = __all__
