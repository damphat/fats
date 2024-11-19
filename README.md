## My personal python utillities
- [x] start an interactive python shell with history and autocompletion
    ```
    fats.interact()
    ```
- [x] plot/update an axis
    ```py
    fats.plot(dict(weights=weights, biases=biases))
    ```
- [x] plot multiple axes in 1 figure
    ```py
    fats.plots(
        dict(weights=weights, biases=biases),
        dict(loss=loss),
    )
    ```
### Installation

```bash
pip install git+https://github.com/damphat/fats.git
```

### Usage

```py
import fats

def foo():
    print('foo')

fats.interact() # start an interactive python shell
```