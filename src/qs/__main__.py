from .qs import read_urls
from .qs import read_urls_input
from .qs import process_urls
from .qs import usage
from sys import argv


def main():
    usage(argv)
    
    if len(argv) == 2:
        urls = read_urls_input()
        my_new_val = argv[1]
        process_urls(urls, my_new_val)

    elif len(argv) == 3:
        urls = read_urls(argv[1])
        my_new_val = argv[2]
        process_urls(urls, my_new_val)
    

if __name__ == '__main__':
    main()

