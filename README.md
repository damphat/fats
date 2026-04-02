# fats

Personal Python utilities.

## Install

```bash
# pip
pip install git+https://github.com/damphat/fats.git

# uv
uv add git+https://github.com/damphat/fats.git
```

## fats.interact

A better `code.interact` for quick debugging and scripts.

- **Auto everything**: Injects `globals()` by default.
- **History & Completion**: Persistent history at `~/.fats_history` and tab completion.
- **Zero dependencies**: Pure standard library.

```python
from fats import interact

# ... your code ...
interact()
```
