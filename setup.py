import os

def makedir(dir):
    if os.path.exists(dir):
        return
    print "creating project directory: " + dir
    os.makedirs(dir)

def makefile(filename, init_url):
    curr_path = filename
    if os.path.exists(curr_path):
        return
    print "creating target file in project: " + curr_path
    f = open(curr_path, 'w')
    f.write(init_url + "\n")
    f.close()

## makedir("test")
## makefile("test/queue","www.google.com")
## makefile("test/crawled", "")

def append_url(filename, new_url):
    if not os.path.exists(filename):
        print filename + " does not exist!"
        return
    f = open(filename, 'a')
    new_url = new_url.encode('ascii', 'ignore')
    f.write(new_url + "\n")
    f.close()

def delete_file(filename):
    if not os.path.exists(filename):
        print filename + " does not exist!"
        return
    f = open(filename, 'w')
    f.close()

def fileToSet(filename):
    if not os.path.exists(filename):
        print filename + " does not exist!"
        return None
    urls = set()
    f = open(filename, 'r')
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        line = line.replace('\n', '')
        urls.add(line)
    f.close()
    return urls

def setToFile(filename, url_set):
    delete_file(filename)
    if url_set is None or len(url_set) == 0:
        return
    for x in sorted(url_set):
        append_url(filename, x)
