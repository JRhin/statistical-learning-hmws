import pandas as pd
from langdetect import detect
import tqdm

df = pd.read_csv('data.csv')

prep_df = pd.DataFrame(columns =['Tweet', 'Label'])

print("Deleting users name and urls:")

for tweet in tqdm.tqdm(df['Tweet']):
    tweet_words = []
    for word in str(tweet).split(' '):
        if word.startswith('@'):
            word = ''
        elif word.startswith('http'):
            word = ''
        elif word.startswith('https'):
            word = ''
        tweet_words.append(word)
    prep_tweet = " ".join(tweet_words)    
    prep_df = pd.concat( [prep_df, pd.DataFrame({"Tweet": [prep_tweet], "Label": 0})], ignore_index = True)

prep_df = prep_df.drop_duplicates()

prep_df = prep_df.dropna()

print("Deleting non english tweets:")

tweets = prep_df['Tweet']

for tweet in tqdm.tqdm(prep_df['Tweet']):
    try:
        language = detect(tweet)
    except:
        prep_df = prep_df[prep_df['Tweet']!=tweet]
        continue
    if language != 'en':
        prep_df = prep_df[prep_df['Tweet']!=tweet]

print("Number of total preprocessed data:", len(prep_df))

prep_df = prep_df.drop_duplicates(subset=['Tweet'])

prep_df.to_csv('prep_data.csv', index = False)
