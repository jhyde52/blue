# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.


# the bucket has all the key-values where the key when converted to a hash fell into that bucket
# we just want to lookup the value that goes with the key we are looking up
def hash_table_add(ht,key,value): #value is searches
    hash_table_get_bucket(ht,key).append([key,value])

def hashtable_update(ht,key,value):
    bucket = hash_table_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1]=value
            return ht # this is super important to remember! if you added one thing you would want to 
        		# save that here but you also need to allow for cases where another thing that was not in the table is added and then save that
    hash_table_add(htable,key,value)        
    return ht

def hash_string(keyword,buckets): #converts a string into a hash so it is easier to index
    hash=0
    for c in keyword:
        hash= (hash +ord(c)) %buckets
    return hash
    
def make_hash_table(nbuckets):
	ht = []
	for i in range(0,nbuckets):
		ht.append([])
	return ht

def hash_table_get_bucket(ht,keyword):
	return ht[hash_string(keyword,len(ht))]  #return the bucket by passing the index of the keyword into the ht/htable

def hash_table_add(ht, key, value):
    hash_table_get_bucket(ht,key).append([key, value])


table = make_hash_table(3)
hash_table_add(table, 'http://www.anniecannons.com', 23)
hash_table_add(table, 'http://www.projectforawesome.com', 17)
hash_table_add(table, 'http://www.fightworldsuck.org/.com', 19)
hash_table_add(table, 'http://www.youtube.com', 23)
print table


print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11

# print hash_table

'''
def make_hashtable(nbuckets):
    i=0
    ht=[]
    while i<nbuckets:
        ht.append([])
        i+=1
    return ht


usually good to write for loop if you can instead of while
alternative way to write this:
loops through 0 to 9

def make_hash_table(nbuckets):
	ht = []
	for i in range(0,nbuckets):
		ht.append([])
	return ht


'''


