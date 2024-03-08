# defining a function that recommends 10 most similar movies
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommendation_for_a_movie(m):
    m = m.lower()
    data = pd.read_csv("data.csv")
    if m not in data['movie_title'].unique():
        return 'This movie is not in our database.\nPlease check if you spelled it correct.'
    else:
        # getting the index of the movie in the dataframe
        i = data.loc[data['movie_title'] == m].index[0]

        # fetching the row containing similarity scores of the movie
        # from similarity matrix and enumerate it

        # sim = np.load('similarity_matrix.npy')
        # lst = list(enumerate(sim[i]))

        cv = CountVectorizer()
        count_matrix = cv.fit_transform(data['comb'])
        # creating a similarity score matrix
        sim = cosine_similarity(count_matrix)
        lst = list(enumerate(sim[i]))


        # sorting this list in decreasing order based on the similarity score
        lst = sorted(lst, key=lambda x: x[1], reverse=True)

        # taking top 1- movie scores
        # not taking the first index since it is the same movie
        lst = lst[1:11]

        # making an empty list that will containg all 10 movie recommendations
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l


if __name__ == "__main__":
    movie_name = "John Carter"
    print(recommendation_for_a_movie(movie_name))
