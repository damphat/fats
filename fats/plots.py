import matplotlib.pyplot as plt
import numpy as np
import torch

def toDict1(y):
    if isinstance(y, dict):
        return y
    elif isinstance(y, np.ndarray):
        if y.ndim == 1:
            return {0: y}
        elif y.ndim == 2:
            return {i: y[:,i] for i in range(y.shape[1])}
        else:
            raise ValueError(f'Unsupported array shape: {y.shape}')
    elif isinstance(y, list):
        return toDict1(np.array(y))
    elif isinstance(y, torch.Tensor):
        return toDict1(y.detach().cpu().numpy())
    else:
        raise TypeError(f'Unsupported type: {type(y)}')


def plot1(o):
    o = toDict1(o)
    n = len(o)
    for i, (k, v) in enumerate(o.items()):
        plt.plot(v, label=k)
        plt.legend()
        plt.grid(True)
        plt.show(block=False)
        
def toDicts(y):
    if isinstance(y, dict):
        return y
    elif isinstance(y, np.ndarray):
        if y.ndim == 0:
            raise ValueError(f'Unsupported array shape: {y.shape}')
        elif y.ndim == 1:
            return {0: y}
        else:
            return {i: y[i] for i in range(y.shape[0])}
    elif isinstance(y, list):
        return toDicts(np.array(y))
    elif isinstance(y, torch.Tensor):
        return toDicts(y.detach().cpu().numpy())
    else:
        raise TypeError(f'Unsupported type: {type(y)}')

def plots(o, num='fat', figsize=None, sharex=None, sharey=None):
    o = toDicts(o)
    n = len(o)
    fig = plt.figure(num=num, figsize=figsize)
    fig.clear()
    axes = fig.subplots(1, n, sharex=sharex, sharey=sharey)
    if n == 1:
        axes = [axes]
    else:
        axes = axes.flatten()
    for i, (k, v) in enumerate(o.items()):
        plt.sca(axes[i])
        plt.title(k)
        plot1(v)
    
    plt.tight_layout()
    plt.show(block=False)
    
def plot(o, num='fat', figsize=None, sharex=None, sharey=None):
    fig = plt.figure(num=num, figsize=figsize)
    fig.clear()
    plot1(o)
    plt.tight_layout()
    plt.show(block=False)
