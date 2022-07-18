import sys

class VersionException(Exception):
    pass

def main():
    print('Hello, World! From Python:' + str(sys.version_info))
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        # intentional fail for Python 3.6
        raise VersionException('Python version 3.6.x is not supported!')


if __name__ == '__main__':
    main()
