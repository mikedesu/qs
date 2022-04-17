from sys import argv
from sys import stderr
from datetime import datetime


def read_urls(filename):
    urls = None
    with open(argv[1],'r') as infile:
        urls = infile.readlines()
    return urls


def usage(a):
    if len(a)!=3:
        print("Usage: python3 qs.py <url_filename> <custom_value>")


def process_url(new_url_base, param_vals, my_new_val):
    for i in range(len(param_vals)):
        pv = param_vals.pop(i)
        pv_split = pv.split("=")
        if len(pv_split)==1:
            continue
        param = pv_split[0]
        new_pv = param + "=" + my_new_val
        param_vals.insert(i, new_pv)
        new_query_str = "&".join(param_vals)
        new_url = new_url_base + new_query_str 
        param_vals.pop(i)
        param_vals.insert(i, pv)
        print(new_url)


def process_urls(urls, my_new_val):
    while len(urls) > 0:
        url = urls.pop()
        url = url[:-1]
        url_split = url.split("?")
        if len(url_split)>1:
            url_base = url_split[0]
            query_str = url_split[1]
            param_vals = query_str.split("&")
            len_param_vals = len(param_vals)
            new_url_base = url_base + "?"
            process_url(new_url_base, param_vals, my_new_val)



