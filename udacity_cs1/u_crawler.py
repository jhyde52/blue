# This program will crawl all the pages from a seed page. It finds all the links
# on the page and follows them and finds more. It keeps track of what it already
# visited and what it needs to visit.
# It also creates a search index by listing all the urls that contain each word
# on each of the pages.

import urllib2

def get_page(url):
    #urllib2.urlopen(url).read()    
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return  '&lt;?xml version="1.0" encoding="utf-8" ?&gt;&lt;?xml-stylesheet href="http://imgs.xkcd.com/s/c40a9f8.css" type="text/css" media="screen" ?&gt;&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"&gt;&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt; &lt;head&gt; &lt;title&gt;xkcd: Python&lt;/title&gt; &lt;link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/c40a9f8.css" media="screen" title="Default" /&gt; &lt;!--[if IE]&gt;&lt;link rel="stylesheet" type="text/css" href="http://imgs.xkcd.com/s/ecbbecc.css" media="screen" title="Default" /&gt;&lt;![endif]--&gt; &lt;link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="/atom.xml" /&gt; &lt;link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="/rss.xml" /&gt; &lt;link rel="icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /&gt; &lt;link rel="shortcut icon" href="http://imgs.xkcd.com/s/919f273.ico" type="image/x-icon" /&gt; &lt;/head&gt; &lt;body&gt; &lt;div id="container"&gt; &lt;div id="topContainer"&gt; &lt;div id="topLeft" class="dialog"&gt; &lt;div class="hd"&gt;&lt;div class="c"&gt;&lt;/div&gt;&lt;/div&gt; &lt;div class="bd"&gt; &lt;div class="c"&gt; &lt;div class="s"&gt;\t&lt;ul&gt; &lt;li&gt;&lt;a href="http://xkcd.com/554""&gt;Archive&lt;/a&gt;&lt;br /&gt;&lt;/li&gt;\t &lt;li&gt;&lt;a href="http://blag.xkcd.com/"&gt;News/Blag&lt;/a&gt;&lt;br /&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="http://store.xkcd.com/"&gt;Store&lt;/a&gt;&lt;br /&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="/about/"&gt;About&lt;/a&gt;&lt;br /&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="http://forums.xkcd.com/"&gt;Forums&lt;/a&gt;&lt;br /&gt;&lt;/li&gt; &lt;/ul&gt; &lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class="ft"&gt;&lt;div class="c"&gt;&lt;/div&gt;&lt;/div&gt; &lt;/div&gt; &lt;div id="topRight" class="dialog"&gt; &lt;div class="hd"&gt;&lt;div class="c"&gt;&lt;/div&gt;&lt;/div&gt; &lt;div class="bd"&gt; &lt;div class="c"&gt; &lt;div class="s"&gt; &lt;div id="topRightContainer"&gt; &lt;div id="logo"&gt; &lt;a href="/"&gt;&lt;img src="http://imgs.xkcd.com/s/9be30a7.png" alt="xkcd.com logo" height="83" width="185"/&gt;&lt;/a&gt; &lt;h2&gt;&lt;br /&gt;A webcomic of romance,&lt;br/&gt; sarcasm, math, and language.&lt;/h2&gt; &lt;div class="clearleft"&gt;&lt;/div&gt; &lt;br /&gt;XKCD updates every Monday, Wednesday, and Friday. &lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class="ft"&gt;&lt;div class="c"&gt;&lt;/div&gt;&lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;div id="contentContainer"&gt; &lt;div id="middleContent" class="dialog"&gt; &lt;div class="hd"&gt;&lt;div class="c"&gt;&lt;/div&gt;&lt;/div&gt; &lt;div class="bd"&gt; &lt;div class="c"&gt; &lt;div class="s"&gt;&lt;h1&gt;Python&lt;/h1&gt;&lt;br/&gt;&lt;br /&gt;&lt;div class="menuCont"&gt; &lt;ul&gt; &lt;li&gt;&lt;a href="/1/"&gt;|&amp;lt;&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="/352/" accesskey="p"&gt;&amp;lt; Prev&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_t"&gt;Random&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="/354/" accesskey="n"&gt;Next &amp;gt;&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="/"&gt;&amp;gt;|&lt;/a&gt;&lt;/li&gt; &lt;/ul&gt;&lt;/div&gt;&lt;br/&gt;&lt;br/&gt;&lt;img src="http://imgs.xkcd.com/comics/python.png" title="I wrote 20 short programs in Python yesterday. It was wonderful. Perl, Im leaving you." alt="Python" /&gt;&lt;br/&gt;&lt;br/&gt;&lt;div class="menuCont"&gt; &lt;ul&gt; &lt;li&gt;&lt;a href="/1/"&gt;|&amp;lt;&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="/352/" accesskey="p"&gt;&amp;lt; Prev&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="http://dynamic.xkcd.com/random/comic/" id="rnd_btn_b"&gt;Random&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="/354/" accesskey="n"&gt;Next &amp;gt;&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href="/"&gt;&amp;gt;|&lt;/a&gt;&lt;/li&gt; &lt;/ul&gt;&lt;/div&gt;&lt;h3&gt;Permanent link to this comic: <a rel="nofollow" href="http://xkcd.com/353/</h3><h3>Image">http://xkcd.com/353/&lt;/h3&gt;&lt;h3&gt;Image</a> URL (for hotlinking/embedding): <a rel="nofollow" href="http://imgs.xkcd.com/comics/python.png</h3><div">http://imgs.xkcd.com/comics/python.png&lt;/h3&gt;&lt;div</a> id="transcript" style="display: none"&gt;[[ Guy 1 is talking to Guy 2, who is floating in the sky ]]Guy 1: You39;re flying! How?Guy 2: Python!Guy 2: I learned it last night! Everything is so simple!Guy 2: Hello world is just 39;print &amp;quot;Hello, World!&amp;quot; 39;Guy 1: I dunno... Dynamic typing? Whitespace?Guy 2: Come join us! Programming is fun again! It39;s a whole new world up here!Guy 1: But how are you flying?Guy 2: I just typed 39;import antigravity39;Guy 1: That39;s it?Guy 2: ...I also sampled everything in the medicine cabinet for comparison.Guy 2: But i think this is the python.{{ I wrote 20 short programs in Python yesterday. It was wonderful. Perl, I39;m leaving you. }}&lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class="ft"&gt;&lt;div class="c"&gt;&lt;/div&gt;&lt;/div&gt; &lt;/div&gt; &lt;div id="middleFooter" class="dialog"&gt; &lt;div class="hd"&gt;&lt;div class="c"&gt;&lt;/div&gt;&lt;/div&gt; &lt;div class="bd"&gt; &lt;div class="c"&gt; &lt;div class="s"&gt; &lt;img src="http://imgs.xkcd.com/s/a899e84.jpg" width="520" height="100" alt="Selected Comics" usemap=" comicmap" /&gt; &lt;map name="comicmap"&gt; &lt;area shape="rect" coords="0,0,100,100" href="/150/" alt="Grownups" /&gt; &lt;area shape="rect" coords="104,0,204,100" href="/730/" alt="Circuit Diagram" /&gt; &lt;area shape="rect" coords="208,0,308,100" href="/162/" alt="Angular Momentum" /&gt; &lt;area shape="rect" coords="312,0,412,100" href="/688/" alt="Self-Description" /&gt; &lt;area shape="rect" coords="416,0,520,100" href="/556/" alt="Alternative Energy Revolution" /&gt; &lt;/map&gt;&lt;br/&gt;&lt;br /&gt;Search comic titles and transcripts:&lt;br /&gt;&lt;script type="text/javascript" src="//www.google.com/jsapi"&gt;&lt;/script&gt;&lt;script type="text/javascript"&gt; google.load(\"search\", \"1\"); google.setOnLoadCallback(function() { google.search.CustomSearchControl.attachAutoCompletion( \"012652707207066138651:zudjtuwe28q\", document.getElementById(\"q\"), \"cse-search-box\"); });&lt;/script&gt;&lt;form action="//www.google.com/cse" id="cse-search-box"&gt; &lt;div&gt; &lt;input type="hidden" name="cx" value="012652707207066138651:zudjtuwe28q" /&gt; &lt;input type="hidden" name="ie" value="UTF-8" /&gt; &lt;input type="text" name="q" id="q" autocomplete="off" size="31" /&gt; &lt;input type="submit" name="sa" value="Search" /&gt; &lt;/div&gt;&lt;/form&gt;&lt;script type="text/javascript" src="//www.google.com/cse/brand?form=cse-search-box&amp;lang=en"&gt;&lt;/script&gt;&lt;a href="/rss.xml"&gt;RSS Feed&lt;/a&gt; - &lt;a href="/atom.xml"&gt;Atom Feed&lt;/a&gt;&lt;br /&gt; &lt;br/&gt; &lt;div id="comicLinks"&gt; Comics I enjoy:&lt;br/&gt; &lt;a href="http://www.qwantz.com"&gt;Dinosaur Comics&lt;/a&gt;, &lt;a href="http://www.asofterworld.com"&gt;A Softer World&lt;/a&gt;, &lt;a href="http://pbfcomics.com/"&gt;Perry Bible Fellowship&lt;/a&gt;, &lt;a href="http://www.boltcity.com/copper/"&gt;Copper&lt;/a&gt;, &lt;a href="http://questionablecontent.net/"&gt;Questionable Content&lt;/a&gt;, &lt;a href="http://achewood.com/"&gt;Achewood&lt;/a&gt;, &lt;a href="http://wondermark.com/"&gt;Wondermark&lt;/a&gt;, &lt;a href="http://thisisindexed.com/"&gt;Indexed&lt;/a&gt;, &lt;a href="http://www.buttercupfestival.com/buttercupfestival.htm"&gt;Buttercup Festival&lt;/a&gt; &lt;/div&gt; &lt;br/&gt; Warning: this comic occasionally contains strong language (which may be unsuitable for children), unusual humor (which may be unsuitable for adults), and advanced mathematics (which may be unsuitable for liberal-arts majors).&lt;br/&gt; &lt;br/&gt; &lt;h4&gt;We did not invent the algorithm. The algorithm consistently finds Jesus. The algorithm killed Jeeves. &lt;br /&gt;The algorithm is banned in China. The algorithm is from Jersey. The algorithm constantly finds Jesus.&lt;br /&gt;This is not the algorithm. This is close.&lt;/h4&gt;&lt;br/&gt; &lt;div class="line"&gt;&lt;/div&gt; &lt;br/&gt; &lt;div id="licenseText"&gt; &lt;!-- &lt;a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/"&gt;&lt;img alt="Creative Commons License" style="border:none" src="http://imgs.xkcd.com/static/somerights20.png" /&gt;&lt;/a&gt;&lt;br/&gt; --&gt; This work is licensed under a &lt;a rel="license" href="http://creativecommons.org/licenses/by-nc/2.5/"&gt;Creative Commons Attribution-NonCommercial 2.5 License&lt;/a&gt;.&lt;!-- &lt;rdf:RDF xmlns="http://web.resource.org/cc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns "&gt;&lt;Work rdf:about=""&gt;&lt;dc:creator&gt;Randall Munroe&lt;/dc:creator&gt;&lt;dcterms:rightsHolder&gt;Randall Munroe&lt;/dcterms:rightsHolder&gt;&lt;dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" /&gt;&lt;dc:source rdf:resource="http://www.xkcd.com/"/&gt;&lt;license rdf:resource="http://creativecommons.org/licenses/by-nc/2.5/" /&gt;&lt;/Work&gt;&lt;License rdf:about="http://creativecommons.org/licenses/by-nc/2.5/"&gt;&lt;permits rdf:resource="http://web.resource.org/cc/Reproduction" /&gt;&lt;permits rdf:resource="http://web.resource.org/cc/Distribution" /&gt;&lt;requires rdf:resource="http://web.resource.org/cc/Notice" /&gt;&lt;requires rdf:resource="http://web.resource.org/cc/Attribution" /&gt;&lt;prohibits rdf:resource="http://web.resource.org/cc/CommercialUse" /&gt;&lt;permits rdf:resource="http://web.resource.org/cc/DerivativeWorks" /&gt;&lt;/License&gt;&lt;/rdf:RDF&gt; --&gt; &lt;br/&gt; This means you\"re free to copy and share these comics (but not to sell them). &lt;a href="/license.html"&gt;More details&lt;/a&gt;.&lt;br/&gt; &lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class="ft"&gt;&lt;div class="c"&gt;&lt;/div&gt;&lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;/body&gt;&lt;/html&gt; '
    except:
        return ""
    return ""    
    
def add_to_index(index,keyword,url):
        if keyword in index:
            index[keyword].append(url) #adds to list of urls 
        else:
            index[keyword]=[url] #or add keyword and url

def add_page_to_index(index,url,content):
    keyword=content.split()
    for item in keyword:
        add_to_index(index,item,url)

def get_next_target(page):
    start_link = page.find('&lt;a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
     
def union(a,b):
    for item in b:
        if item not in a:
            a.append(item)

def get_all_links(page):
    links =[]
    while True:
        url, end_pos = get_next_target(page)
        if url:
            links.append(url)
            page = page[end_pos:]
        else: 
            break
    #print links
    return links

def crawl_web(seed):
    tocrawl=[seed]
    crawled=[]
    index =[]
    while tocrawl:
        page=tocrawl.pop() #depth first search (go deep first then go back)
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            union(tocrawl,get_all_links(content))
            crawled.append(page) #add to list of what we crawled
            
    #print crawled
    #print index
    return index
    return crawled
    
def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    else:
       return None


    print lookup(index,'udacity')


print crawl_web("http://www.udacity.com/cs101x/index.html")




#while tocrawl:
#returns True if not empty


