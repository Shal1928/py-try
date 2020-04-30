import os
from beeprint import pp
from core import Args, cfg
from core.const import ENV, PATH
from core.helpers import parse_sys_args

print('Initialization app package started')

print('Parsing script arguments to app_args')
app_args = Args()
parse_sys_args((('-r', '--root'), ('-i', '--integration')), app_args)
if app_args.root is None:
    app_args.root = PATH.PROJECT_PARENT_FOLDER
if app_args.integration is None:
    app_args.integration = app_args.root
pp(app_args)

print('Updating configuration Local section')
cfg[ENV.LOCAL]['common-app'] = os.path.normpath(app_args.integration + cfg[ENV.LOCAL]['common-app'])
print('Configuration Local section is updated:')
pp(cfg)
