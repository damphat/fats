## My personal python utillities
- [x] start an interactive python shell with history and autocompletion
    ```
    fats.interact()
    ```
- [x] plot/update an axis
    ```py
    fats.plot(dict(
        inputs=inputs, 
        outputs=outputs,
    ))
    ```
- [x] plot multiple axes in 1 figure
    ```py
    fats.plots(dict(
        inputs=inputs,
        outputs=outputs,
        losses=dict(
            train_losses=train_losses,
            val_losses=val_losses,
        ),
    ))
    ```
### Installation

```bash
pip install git+https://github.com/damphat/fats.git
```

### Usage

```py
import torch
import fats

inputs = torch.randn(10, 2)
outputs = torch.randn(10, 1)
losses = torch.randn(10)

fats.plot(dict(inputs=inputs, outputs=outputs))
fats.plots(dict(
    ax1=dict(inputs=inputs, outputs=outputs),
    losses=losses,
))

fats.interact() # start an interactive python shell
```