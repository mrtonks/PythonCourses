# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Pyscho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# album, artist, year, tracks = imelda
# # print(tracks[0][0])
# # print(len(tracks))
# print("Album: {}\nArtist: {}\nYear: {}".format(album, artist, year))
#
# for song in tracks:
#     track, title = song
#     print("\tTrack #{}: {}".format(track, title))

imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Pyscho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

imelda[3].append((5, "All For You"))

album, artist, year, tracks = imelda
# print(tracks[0][0])
# print(len(tracks))
print("Album: {}\nArtist: {}\nYear: {}".format(album, artist, year))

for song in tracks:
    track, title = song
    print("\tTrack #{}: {}".format(track, title))
