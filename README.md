# Settings
A dead-useful settings class used in nearly all of my projects.  

## Install

Assuming the use of [poetry](https://python-poetry.org/):
`poetry add git+https://github.com/LSaldyt/settings#main`

Usage:
``` 
from settings import Settings
my_settings = Settings(learning_rate=1e-3, my_hyperparam=3)
print(my_settings)
ablation = my_settings.derive(my_hyperparam=0)
print(ablation)
```

