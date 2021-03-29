import math
import matplotlib.pyplot as plt


class GridPlot:

    def __init__(self, ncols=10, width=10):
        self.ncols = ncols
        self.width = width
        self.images = []

    def imshow(self, image):
        self.images.append(image)

    def show(self):

        N = len(self.images)
        ncols = self.ncols
        nrows = math.ceil(N / ncols)

        width = self.width
        height = width * (nrows / ncols)

        # plt.cla()
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(width, height))

        for n, image in enumerate(self.images):
            col = n % ncols
            row = n // ncols
            axes[row, col].axis('off')
            axes[row, col].imshow(image)

        plt.show()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_type is None:
            self.show()
