# jplotlib
Quick plotting utilities

## Installing

`$ pip install jplotlib`

## Example

```python
import numpy as np
import jplotlib as jpl

with jpl.GridPlot(width=20) as ig:
    for _ in range(50):
        ig.imshow(np.random.uniform(size=(100, 100, 3)))
```
![output](https://raw.githubusercontent.com/JacobFV/jplotlib/main/content/images/grid_plot_example.png)