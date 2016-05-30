import sys

sys.path[0:0] = ['.', '..']

from executors import executor


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        similarity = executor.execute(argv[1])
    except IOError:
        print('Wrong path to source directory')
    except AttributeError as e:
        print("Check for values of plugins at src/settings.json\n", e)
    print('Similarity:')
    for key in similarity.keys():
        print(key, similarity[key])


if __name__ == "__main__":
    sys.exit(main())
