import sys

sys.path[0:0] = ['.', '..']

from executors import executor


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        print('Similarity:', executor.execute(argv[1]))
    except IOError:
        print('Wrong path to source directory')


if __name__ == "__main__":
    sys.exit(main())
