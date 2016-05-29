import sys

sys.path[0:0] = ['.', '..']

from executors import executor


def main(argv=None):
    if argv is None:
        argv = sys.argv
    print('Similarity:', executor.execute(argv[1]))


if __name__ == "__main__":
    sys.exit(main())
