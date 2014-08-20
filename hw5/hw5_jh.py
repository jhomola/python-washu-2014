# Scraper to collect petition info from andrewgelman.com
from BeautifulSoup import *
import sys, csv, operator, re, urllib2, time
from nltk.util import clean_html
from datetime import datetime

# What page? 
page_to_scrape = 'http://andrewgelman.com/'

# What info do we want? 
headers = ["is_post", "publish_date", "author", "url", "post_title", "comment_count"]

# Where do we save info?
filename = "hw5_jh.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# Open webpage
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	   
while True:
	req = urllib2.Request(page_to_scrape, headers=hdr)
	webpage = urllib2.urlopen(req)

# Parse it
	soup = BeautifulSoup(webpage.read())
	soup.prettify()

# Extract titles
	titles = soup.findAll("h2", attrs={'class':'posttitle'})

# Extract date
	dates = soup.findAll("span", attrs={'class':'postdate'}) 
  
# Extract author
	authors = soup.findAll("span", attrs={'class':'postauthor'})
  
# Extract url
	urls = soup.findAll("h2", attrs={'class':'posttitle'})
  
# Extract comments
	comments = soup.findAll("span", attrs={'class':'postcomment'})

	
	for i in range(len(titles)):
		title = titles[i]
		t = clean_html(str(title.find("a")))
		date = dates[i]
		d = clean_html(str(date))
		d = datetime.strptime(d, "%d %B %Y, %I:%M %p")		#converts it into standard date time format
		a = authors[i]
		a = clean_html(str(a.find("a")))
		url = urls[i]
		u = url.find("a").get("href")
		comment = comments[i]
		c = clean_html(str(comment.find("a")))
		c = re.findall(r"\d\S*", c)
		if c == []: c = 0
		else: c = int(c[0])
		ispost = False
		if (len(t) != 0) & (len(str(d)) != 0) & (len(u) != 0) & (isinstance(c, int)): ispost = True
		csvwriter.writerow([ispost, d, a, u, t, c])

#Next page		
	next = soup.findAll("div", attrs={'class':'alignleft'})
	for i in next:
		nextpage = i.find("a").get("href")
	if int(nextpage.split("/")[4]) > 10: break		# scrape first 10 pages, then break
	else: 
		time.sleep(5)
		print nextpage.split("/")[4]
		page_to_scrape = nextpage
		
  
readFile.close()

#Open csv file again and sort by date
data = csv.reader(open('hw5_jh.csv'),delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(1), reverse=True)
with open("hw5sorted_jh.csv", "wb") as f:
	fileWriter = csv.writer(f, delimiter=',')
	for row in sortedlist:
		fileWriter.writerow(row)