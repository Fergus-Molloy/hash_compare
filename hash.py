import sys
import os.path

def compare(file, hash):
    file_hash=sys.subprocess.check_output(['CertUtil', '-hashfile', file, 'MD5'])
    return (file_hash==hash)


if __name__ == "__main__":
    if(os.path.isfile(sys.argv[1])):
        print(compare(sys.argv[1], sys.argv[2]))
    elif(os.path.isfile(sys.argv[2])):
        print(compare(sys.argv[2], sys.argv[1]))
    else:
        print("file not supplied")
