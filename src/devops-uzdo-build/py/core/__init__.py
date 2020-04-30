from core.const import PATH
from core.helpers import get_cfg

print('Initialization core package started')


class Args:
    pass


cfg = get_cfg(PATH.ENV_CFG)
print(f'Configuration: {PATH.ENV_CFG} loaded')
