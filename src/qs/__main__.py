from .qs import read_urls
from .qs import process_urls
from .qs import usage
from sys import argv


def main():
    usage(argv)
    urls = read_urls(argv[1])
    my_new_val = argv[2]
    process_urls(urls, my_new_val)
    

if __name__ == '__main__':
    main()

