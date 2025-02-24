from .cifar import Cifar10 as Cifar10, Cifar100 as Cifar100
from .flowers import Flowers as Flowers
from .folder import DatasetFolder as DatasetFolder, ImageFolder as ImageFolder
from .mnist import FashionMNIST as FashionMNIST, MNIST as MNIST
from .voc2012 import VOC2012 as VOC2012

__all__ = ['DatasetFolder', 'ImageFolder', 'MNIST', 'FashionMNIST', 'Flowers', 'Cifar10', 'Cifar100', 'VOC2012']
