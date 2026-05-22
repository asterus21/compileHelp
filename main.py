import argparse
from data import Defaults
from script import start_script, script_start
from misc import *


if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--license',  action='store',      dest='license', help='path to a licence file',  type=str, default=Defaults.LICENSE)
    parser.add_argument('-b', '--build',    action='store',      dest='build',   help='path to a builds folder', type=str, default=Defaults.BUILDS)
    parser.add_argument('-s', '--script',   action='store',      dest='script',  help='path to a script file',   type=str, default=Defaults.SCRIPT)
    parser.add_argument('-n', '--number',   action='store',      dest='number',  help='path to a build folder number for a default builds path',  type=str, default=None) 
    parser.add_argument('-d', '--defaults', action='store_true', dest='default', help='show default values')


    args = parser.parse_args()

    if args.default:
        print(f'License path: {Defaults.LICENSE}')
        print(f'Builds path:  {Defaults.BUILDS}')
        print(f'Script path:  {Defaults.SCRIPT}')
    elif args.number:
        paths = [args.build, args.number]
        path = '/'.join(paths)
        command = f'{args.script}'
        env = set_env(f'{path}/Bin64/nodejs', args.license, f'{path}/SourceData')
        script_start(path, command, env=env)
    else:
        build_path, cmd, env = start_script(builds=args.build, license=args.license, script=args.script)
        script_start(build_path, cmd, env=env)
