import os
import sys


class MetaConst(type):
    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        raise TypeError


class Const(object, metaclass=MetaConst):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError


class ENV(Const):
    LOCAL = 'Local'
    SERVER = 'Server'
    STANDS = 'Stands'


class PATH(Const):
    LVL_UP = '../'
    SCRIPT_FOLDER = sys.path[0]
    ENV_CFG = os.path.join(SCRIPT_FOLDER, 'env.cfg')
    PROJECT_PARENT_FOLDER = os.path.normpath(os.path.join(SCRIPT_FOLDER, LVL_UP * 3))
