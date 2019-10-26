import sys
import spotipy
import spotipy.util as util
import billboard
scope = 'user-library-read'
song_names = []


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: {} username".format(sys.argv[0]))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

chart = billboard.ChartData('hot-100')
if token:
    sp = spotipy.Spotify(auth=token)

    for i in range(len(chart)):
        results = sp.search(q=chart[i].title, limit=1)
        for i, t in enumerate(results['tracks']['items']):
            print (' ', i, t['id'],t['name'])
            

    
    #print(sp.audio_analysis("1xzBco0xcoJEDXktl7Jxrr"))
else:
    print ("Can't get token for", username)