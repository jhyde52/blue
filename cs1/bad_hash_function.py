
import urllib2



def get_page(url):
   return urllib2.urlopen(url).read()

def bad_hash_string(keyword, buckets):
	return ord(keyword[0]) %buckets

def test_hash_string(func,keys,size):
	results = [0]*size
	keys_used = []
	for w in keys:
		if w not in keys_used:
			hv=func(w,size)
			results[hv] += 1
			keys_used.append(w)
	return results

words = get_page('http://gutenberg.org/cache/epub/1661/pg1661.txt').split()
counts = test_hash_string(bad_hash_string,words,12)
print counts


# how are there more than 12 buckets when there are only
# 0-9 that could be returned by a modulus operation?


