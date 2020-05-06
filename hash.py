import subprocess
import sys
import os.path

def compare(file, Hash:str):
    #get hash of file provided
    file_hash=(subprocess.check_output(['CertUtil', '-hashfile', file, 'MD5']).decode("utf-8")).split('\n')
    #should print lined up for easy verification
    print(file_hash[1])
    print(Hash)
    # == comparator doesn't work for some reason
    for x in range(len(file_hash[1])-1):
        if(file_hash[1][x] != Hash[x]):
            print(file_hash[1][x])
            print(Hash[x])
            return False
    return True

if __name__ == "__main__":
    # doesn't matter which way round you put the file
    if(os.path.isfile(sys.argv[1])):
        print(compare(sys.argv[1], sys.argv[2]))
    elif(os.path.isfile(sys.argv[2])):
        print(compare(sys.argv[2], sys.argv[1]))
    else:
        print("file not supplied")
