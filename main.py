from flask import Flask, jsonify

app = Flask(__name__)

class Album:
    def __init__(self, id, title, year, artist_id):
        self.id = id
        self.title = title
        self.year = year
        self.artist_id = artist_id

class Song:
    def __init__(self, id, title, duration, album_id):
        self.id = id
        self.title = title
        self.duration = duration
        self.album_id = album_id

albums = [
    Album(1, 'Highway 61 Revisited', 1965, 1),
    Album(2, 'Blonde on Blonde', 1966, 1),
    Album(3, 'Blood on the Tracks', 1975, 1)
]

songs = [
    Song(1, 'Like a Rolling Stone', '6:13', 1),
    Song(2, 'Tangled Up in Blue', '5:42', 3),
    Song(3, 'Knockin\' on Heaven\'s Door', '2:32', 3)
]

@app.route('/albums', methods=['GET'])
def get_albums():
    bob_dylan_albums = [{'id': album.id, 'title': album.title, 'year': album.year} for album in albums if album.artist_id == 1]
    return jsonify(bob_dylan_albums)

@app.route('/songs', methods=['GET'])
def get_songs():
    bob_dylan_songs = [{'id': song.id, 'title': song.title, 'duration': song.duration} for song in songs if song.album_id in [album.id for album in albums if album.artist_id == 1]]
    return jsonify(bob_dylan_songs)

@app.route('/healthcheck', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'})


if __name__ == '__main__':
    app.run(debug=True)

