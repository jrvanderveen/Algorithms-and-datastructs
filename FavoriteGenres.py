#####
# I: dict[userName] = [list of songs], dict[genre] = [list of songs]
# O: dict[userName] = [list of genres].sort(num times listened to genre) only the hightest listened to genre(s)
# C: assuming no duplicate songs in list
# E: user listed to no songs, songs may not have a genre in dict
#####

'''
Need to reverse the mapping of genres to songs
then look through each user and their songs and create dict[genre] = count and then append the results with the user name
then sort the dict and return
'''
import heapq
from collections import defaultdict
userSongs1 = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma":  ["song5", "song6", "song7"]
}
songGenres1 = {
    "Rock":    ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno":  ["song2", "song4"],
    "Pop":     ["song5", "song6"],
    "Jazz":    ["song8", "song9"]
}


class Solution(object):
    def userGenreList(self, userSongs, songGenres):
        songGenresRev = defaultdict(list)
        returnDict = defaultdict(list)
        for genre in songGenres.keys():
            for song in songGenres[genre]:
                songGenresRev[song].append(genre)

        for user in userSongs.keys():
            userGenres = defaultdict(int)
            m = 0
            for song in userSongs[user]:
                for genres in songGenresRev[song]:
                    userGenres[genres] += 1
                    m = max(userGenres[genres], m)

            for genre in userGenres.keys():
                if userGenres[genre] == m:
                    returnDict[user].append(genre)

        return dict(returnDict)


print(Solution().userGenreList(userSongs1, songGenres1))
