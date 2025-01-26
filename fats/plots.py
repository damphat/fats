import matplotlib.pyplot as plt
import numpy as np
import torch

def toDict1(y):
    if isinstance(y, dict):
        return y
    elif isinstance(y, np.ndarray):
        if y.ndim == 0:
            raise ValueError(f'Unsupported array shape: {y.shape}')
        elif y.ndim == 1:
            return {0: y}
        elif y.ndim == 2:
            return {i: y[:,i] for i in range(y.shape[1])}
        elif y.ndim == 3:
            return {(i,j): y[:,i,j] for i in range(y.shape[1]) for j in range(y.shape[2])}
        else:
            raise ValueError(f'Unsupported array shape: {y.shape}')
    elif isinstance(y, list):
        return {i: y[i] for i in range(len(y))}
    elif isinstance(y, torch.Tensor):
        return toDict1(y.detach().cpu().numpy())
    else:
        raise TypeError(f'Unsupported type: {type(y)}')


def plot1(o):
    o = toDict1(o)
    n = len(o)
    for i, (k, v) in enumerate(o.items()):
        plt.plot(v.reshape(v.shape[0], -1), label=k)
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
        return {i: y[i] for i in range(len(y))}
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

def plotLoss(train_loss, val_loss = None, yscale='log'):
    plt.yscale(yscale)
    plt.title(f'Loss {train_loss[-1]:.5f}')
    plt.plot(train_loss, label='train')
    if val_loss is not None:
        plt.plot(val_loss, label='val')
    plt.legend()
    plt.grid(True)
    
def plotOutput(x, y, y_pred):
    plt.title('Output')
    plt.plot(x, y, label='y')
    plt.plot(x, y_pred, label='y_pred')
    plt.legend()
    plt.grid(True)
    
def scatterOutput(x, y, y_pred):
    plt.title('Output')
    plt.scatter(x, y, label='y')
    plt.scatter(x, y_pred, label='y_pred')
    plt.legend()
    plt.grid(True)
    