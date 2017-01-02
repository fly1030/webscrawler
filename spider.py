import urllib
import urllib2
from setup import *
from collect_url import *
import re

class Spider(object):
    ### global variables shared among all spiders
    ### all spiders share same target/visited URLs
    #### target_url/ target_set, visited_url/visited_set
    project = ''
    baseurl = ''
    target_url = ''
    visited_url = ''
    domain = ''
    target_set = set()
    visited_set = set()

    def __init__(self, project, domain, baseurl):
        Spider.project = project
        Spider.domain = domain
        Spider.baseurl = baseurl
        Spider.target_url =  Spider.project + "/target.txt"
        Spider.visited_url = Spider.project + "/visited.txt"
        self.startEngine()
        self.crawl("Initiated Spider", Spider.baseurl)

    def startEngine(self):
        ### First spider to create project structures below
        makedir(Spider.project)
        makefile(Spider.target_url, Spider.baseurl)
        makefile(Spider.visited_url, "")
        Spider.target_set = fileToSet(Spider.target_url)

    def crawl(self, thread, url):
        if url in Spider.visited_set:
            return
        print thread + ": " + "Processing " + url
        self.addFoundLinks(url)
        Spider.target_set.remove(url)
        Spider.visited_set.add(url)
        print "Number of crawled links: " + str(len(Spider.visited_set))
        print "Number of target links: " + str(len(Spider.target_set))
        setToFile(Spider.target_url, Spider.target_set)
        setToFile(Spider.visited_url, Spider.visited_set)

    def addFoundLinks(self, url):
        html_output = ""
        try:
            response = urllib.urlopen(url)
            test = response.headers['Content-Type'].find("text/html")
            if test != -1:
                html_orig = response.read()
                html_output = html_orig.decode("utf-8")
            newLinks = CollectUrl(Spider.baseurl, url)
            newLinks.feed(html_output)

        except:
            print "cannot access page"
            return

        all_new_url = newLinks.output()
        for link in all_new_url:
            if link in Spider.target_url:
                continue
            if link in Spider.visited_url:
                continue
            Spider.target_set.add(link)


