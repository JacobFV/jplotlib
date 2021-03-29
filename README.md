# jplotlib
Quick plotting utilities

## Installing

`$ pip install jplotlib`

## Example

```python
import numpy as np
import jplotlib as jpl

with jpl.GridPlot(width=20) as grid_plot:
    for _ in range(50):
        grid_plot.imshow(np.random.uniform(size=(100, 100, 3)))
```
![output](https://raw.githubusercontent.com/JacobFV/jplotlib/main/content/images/grid_plot_example.png)
