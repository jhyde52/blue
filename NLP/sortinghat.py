# Import modules
import pandas as pd
import requests

# Get Ravenclaw articles using an API call on the wiki site: http://harrypotter.wikia.com/api/v1/
category = 'Ravenclaws'
url = 'http://harrypotter.wikia.com/api/v1/Articles/List?expand=1&limit=1000&category=' + category
requested_url = requests.get(url)
json_results = requested_url.json()
info = json_results['items']
ravenclaw_df = pd.DataFrame(info)

print('Number of articles: {}'.format(len(info)))
print('')
ravenclaw_df.head()
# There are 148 articles with Rawenclaws in the url


# Set variables
houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
mydf = pd.DataFrame()

# Gets article ids, article url, and house
for house in houses:
    url = "http://harrypotter.wikia.com/api/v1/Articles/List?expand=1&limit=1000&category=" + house + 's'
    requested_url = requests.get(url)
    json_results = requested_url.json()
    info = json_results['items']

    house_df = pd.DataFrame(info)
    house_df = house_df[house_df['type'] == 'article']
    house_df.reset_index(drop=True, inplace=True)
    house_df.drop(['abstract', 'comments', 'ns', 'original_dimensions', 'revision', 'thumbnail', 'type'], axis=1, inplace=True)
    house_df['house'] = pd.Series([house]*len(house_df))
    mydf = pd.concat([mydf, house_df])

mydf.reset_index(drop=True, inplace=True)

# Print results
print('Number of student articles: {}'.format(len(mydf)))
print('')
print(mydf.head())
print('')
print(mydf.tail())
# There are articles about 748 students


