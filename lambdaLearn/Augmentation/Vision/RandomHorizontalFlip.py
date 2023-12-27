import numpy as np
import PIL.Image
import torch
from torchvision import transforms

from lambdaLearn.Base.Transformer import Transformer


class RandomHorizontalFlip(Transformer):
    def __init__(self):
        super().__init__()
        self.augmentation=transforms.RandomHorizontalFlip()

    def transform(self,X=None):
        if isinstance(X,np.ndarray):
            X=PIL.Image.fromarray(X)
        if isinstance(X,PIL.Image.Image):
            X = self.augmentation(X)
            return X
        elif isinstance(X,torch.Tensor):
            if len(X.shape)==4:
                for _ in range(X.shape[0]):
                    X[_]=self.augmentation(X[_])
            else:
                X = self.augmentation(X)
            return X
        else:
            raise ValueError('No data to augment')
