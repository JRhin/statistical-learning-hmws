import snscrape.modules.twitter as sntwitter
import pandas as pd
import tqdm

queries = ['flower', 'plant', 'cloud', 'montain', 'sea', 'moon', 'sand', 'motherfucker', 'dickhead', 'dick',
           'fat', 'suck my dick', 'fucker', 'kill your self', 'niggers', 'bang your mom', 'whore', 'fuck you',
           'hope you die', 'just die', 'death', 'kill', 'fuck', 'shit', 'pussy', 'cancer', 'love',
          'hate', 'moron', 'balls', 'suck my balls', 'rape', 'asshole', 'bitch']
tweets = []
limit = 1500

for query in tqdm.tqdm(queries):
    count = 0
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if count  == limit:
            break
        else:
            tweets.append([tweet.content])
            count += 1

df = pd.DataFrame(tweets, columns = ['Tweet'])

df.to_csv('n_data.csv', index = False)
