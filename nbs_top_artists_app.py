from spyre import server

import sqlite3 as lite
import pandas as pd


class TopArtistsApp(server.App):
    title = "Top Artists"
    inputs = [
        {
            'label': 'Network',
            'type': 'dropdown',
            'options': [
                {'label': 'Facebook Page Likes', 'value': 'FaceBookPageLikes'},
                {'label': 'Twitter Followers', 'value': 'TwitterFollowers'},
                {'label': 'Youtube Views', 'value': 'YouTubeViews'},
                {'label': 'Instagram Followers', 'value': 'InstagramFollowers'},
                {'label': 'Instagram Likes', 'value': 'InstagramLikes'},
            ],
            'key': 'network',
            'action_id': 'top_artists'

        }, {
            'label': 'limit',
            'type': 'slider',
            'max': 100,
            'value': 30,
            'key': 'n',
            'action_id': 'top_artists'
        }

    ]

    outputs = [{
        'type': 'table',
        'id': 'top_artists'

    }]

    def get_social_data(self):
        con = lite.connect('nbs.db')
        artists_query = "select id, name from artists"
        artists_df = pd.read_sql(artists_query, con)

        socail_query = "select * from social_data"
        social_df = pd.read_sql(socail_query, con)
        df_merged = pd.merge(artists_df, social_df, left_on='id', right_on='artist_id')
        return df_merged.drop(['id', 'artist_id'], axis=1)

    def top_artists(self, params):
        n = int(params['n'])
        network = params['network']
        """return the top n artists from network"""
        df_social = self.get_social_data()  # get the data from sql

        # sort the result by the given network in descending order
        df_sorted = df_social.sort_values(by=network, ascending=False)

        # limit the results to the top n artists
        df_limited = df_sorted.head(n)

        # convert the values to integers so they look nicer
        df_limited.loc[:, network] = df_limited.loc[:, network].astype('int')

        # return the results but just include the values for the network of interest
        return df_limited[['name', network]]


app = TopArtistsApp()
app.launch()
