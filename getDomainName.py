import urlparse

def getDomainName(url):
    try:
        result = urlparse.urlparse(url)
        ## ParseResult(scheme='http', netloc='', path='', params='', query='', fragment='')
        domain = result[1]
        temp = domain.split(".")
        final = temp[-2] + "." + temp[-1]
        return final
    except:
        return ""

##simple testcase for current module
##temp = getDomainName("http://www.google.com")
##print temp
