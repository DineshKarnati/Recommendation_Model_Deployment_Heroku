import pandas as pd
import numpy as np
if __name__ == "__main__":
    df = pd.read_csv("movie_metadata.csv")

    print(df.columns)

    # keeping the columns that are useful in recommndation system
    data = df.loc[:, ['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name', 'genres', 'movie_title']]

    # Checking null values wrt columns
    print(data.isnull().sum(axis=0))

    # replacing null values in the all columns with string 'unknown'
    data['actor_1_name'] = data['actor_1_name'].replace(np.nan, 'unknown')
    data['actor_2_name'] = data['actor_2_name'].replace(np.nan, 'unknown')
    data['actor_3_name'] = data['actor_3_name'].replace(np.nan, 'unknown')
    data['director_name'] = data['director_name'].replace(np.nan, 'unknown')


    # replacing ‘|’ in ‘genres’ column with whitespace, so the genres would be considered different strings.
    data['genres'] = data['genres'].replace('|', ' ')

    # Now converting the ‘movie_title’ columns values to lowercase for searching simplicity.
    data['movie_title'] = data['movie_title'].str.lower()


    # all the movie_title values have a special character added to the end  which needs to be removed
    print(data['movie_title'][0])
    data['movie_title'] = data['movie_title'].str[:-1]
    data.to_csv('data.csv',index=False)
