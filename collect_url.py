from HTMLParser import HTMLParser
import urlparse

class CollectUrl(HTMLParser):

    def __init__(self, baseurl, url):
        HTMLParser.__init__(self)
        self.baseurl = baseurl
        self.url = url
        self.collections = set()

##    def error(self, message):
##        print message
##        return

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        else:
            for elem in attrs:
                label = elem[0]
                value = elem[1]
                if label == "href":
                    newurl = urlparse.urljoin(self.baseurl, value)
                    self.collections.add(newurl)

    def output(self):
        return self.collections

## Simple testcase for current module
##instance = CollectUrl("http://borderxlab.com", "http://borderxlab.com/blog/")
##instance.feed('<html><head><title>Test</title></head>'
##              '<body><h1>Parse me!</h1><a href = "http://www.borderxlab.com/contactus"></a></body></html>')
##all = instance.output()
##print all
