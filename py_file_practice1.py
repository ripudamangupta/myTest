import sys
import os

def fsearch(fname,skey):
    print(fname,skey)
    if os.path.isfile(fname):
        with open(fname, 'r') as log_file:
            fcontent = log_file.readlines()
            cnt = 0
            for fline in fcontent:
                if skey in fline:
                    cnt += 1
        return(['Success',cnt])
    else:
        return(['Fail',0])

def main(fname,skey):
    skey_result = fsearch(fname,skey)
    print(skey_result[0], skey_result[1])


if __name__ == '__main__':
    fname = sys.argv[1]
    skey = sys.argv[2]
    main(fname,skey)
    

