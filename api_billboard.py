import sys
import spotipy
import spotipy.util as util
import billboard
scope = 'user-library-read'
song_names = []

chart = billboard.ChartData('hot-100')