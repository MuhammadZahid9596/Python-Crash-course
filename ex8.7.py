def make_album(artist_name,album_title,num_tracks=''):
        mydic = {}
        if num_tracks:

            mydic['name']=artist_name
            mydic['album'] = album_title
            mydic['number of tracks']=num_tracks
            return mydic
        else:
            mydic['name']=artist_name
            mydic['album']=album_title
            return mydic


print(make_album('zahid','good',3))
print(make_album('usman','cool'))
print(make_album('xeerak','blaster'))
