from copy import deepcopy, copy
from pprint import pprint, pformat
import subprocess

class Settings:
    def __init__(self, **kwargs):
        self.params = dict(**kwargs)
        self.params['version'] = subprocess.check_output(['git', 'describe', '--always']).strip()

    def update(self, **kwargs):
        self.params.update(**kwargs)

    def derive(self, **kwargs):
        self_copy = Settings()
        self_copy.params = deepcopy(self.params)
        self_copy.update(**kwargs)
        return self_copy

    def show(self):
        pprint(self.params)

    def export(self, parent):
        ''' Be careful with this one :) '''
        parent.update(self.params)

    def __str__(self):
        return pformat(self.params)

    def __repr__(self):
        return str(self)

    def __getattr__(self, name):
        try:
            return self.params[name]
        except KeyError:
            try:
                return object.__getattr__(self, name)
            except:
                raise AttributeError(f'The attribute {name} is not defined in Settings {self}')

    ''' The below two functions are needed if recursive Settings objects are desired.  '''

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result
