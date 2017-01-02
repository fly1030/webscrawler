import threading
import Queue
from setup import *
from collect_url import *
from spider import *
from getDomainName import *

##PROJECT = "borderx"
##BASEURL = "http://borderxlab.com"
NUM_OF_THREADS = 8
threads = Queue.Queue()

## User interface:
PROJECT = raw_input("Define project name: ")
BASEURL = raw_input("Define initial start URL link: ")
DOMAIN = getDomainName(BASEURL)
TARGETURL = PROJECT + "/target.txt"
VISITEDURL = PROJECT + "/visited.txt"

## create the first spider to launch the engine and create the structures
firstspider = Spider(PROJECT, DOMAIN, BASEURL)
##targeturl_set = fileToSet(TARGETURL)
def update_threads():
    for page in Spider.target_set:
        threads.put(page)
    threads.join()
    process()


## update threads while there is more jobs to process in queue
def process():
    if len(Spider.target_set) != 0:
        update_threads()

## create multiple Spiders
def create_threads():
    for i in range(0, NUM_OF_THREADS):
        new = threading.Thread(target = crawlpage)
        ## make it daemon, when main exists job ends
        new.daemon = True
        new.start()

## crawl pages in target set
def crawlpage():
    while 1 > 0:
        curr_url = threads.get()
        Spider.crawl(firstspider, threading.currentThread().name, curr_url)
        threads.task_done()

## main {
create_threads()
process()
## }
