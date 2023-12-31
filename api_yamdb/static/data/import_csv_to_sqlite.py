import sqlite3

import pandas as pd

con = sqlite3.connect('api_yamdb/db.sqlite3')
cur = con.cursor()

category = pd.read_csv('api_yamdb/static/data/category.csv',
                       header=0,
                       index_col=0,
                       names=('id', 'name', 'slug'))
category.to_sql('reviews_category', con, if_exists='append',
                index_label='id')

genre = pd.read_csv('api_yamdb/static/data/genre.csv',
                    header=0,
                    index_col=0,
                    names=('id', 'name', 'slug'))
genre.to_sql('reviews_genre', con, if_exists='append', index_label='id')

title = pd.read_csv('api_yamdb/static/data/titles.csv')
title['description'] = ''
title.to_csv('api_yamdb/static/data/titles.csv', index=False)
title = pd.read_csv('api_yamdb/static/data/titles.csv',
                    header=0,
                    index_col=0,
                    names=('id', 'name', 'year', 'category_id', 'description'))
title.to_sql('reviews_title', con, if_exists='append', index_label='id')

genre_title = pd.read_csv('api_yamdb/static/data/genre_title.csv',
                          header=0,
                          index_col=0,
                          names=('id', 'titles_id', 'genres_id'))
genre_title.to_sql('reviews_titlegenre',
                   con, if_exists='append', index_label='id')

# для модели review
review = pd.read_csv('api_yamdb/static/data/review.csv',
                     header=0,
                     index_col=0,
                     names=(
                         'id', 'title_id', 'text', 'author_id', 'score',
                         'pub_date'))
review.to_sql('reviews_review',
              con, if_exists='append', index_label='id')

# для модели comment
comments = pd.read_csv('api_yamdb/static/data/comments.csv',
                       header=0,
                       index_col=0,
                       names=('id', 'review_id', 'text',
                              'author_id', 'pub_date'))
comments.to_sql('reviews_comment',
                con, if_exists='append', index_label='id')

# для модели user - определить название модели
users = pd.read_csv('api_yamdb/static/data/users.csv',
                    header=0,
                    index_col=0,
                    names=(
                        'id', 'username', 'email', 'role', 'bio', 'first_name',
                        'last_name'))
users.to_sql('users_user',
             con, if_exists='append', index_label='id')

con.commit()
