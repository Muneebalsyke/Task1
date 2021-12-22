import csv
import string


class Movies:

    def __init__(self, movielist):
        self.movielist = movielist
        self.id = self.movielist[0]
        self.titletype = self.movielist[1]
        self.orgtitle = self.movielist[2]
        self.startyear = self.movielist[3]
        self.runtime = self.movielist[4]
        self.genre = self.movielist[5]
        self.rating = self.movielist[6]
        self.numvotes = self.movielist[7]

    def movie_parser(self, movielist):
        self.id = str(movielist[0])
        self.titletype = str(movielist[1])
        self.orgtitle = str(movielist[2])
        self.startyear = int(movielist[3])
        self.runtime = int(movielist[4])
        self.genre = str(movielist[5])
        self.rating = float(movielist[6])
        self.numvotes = int(movielist[7])

    def get_id(self):
        return self.id

    def get_titletype(self):
        return self.titletype

    def get_originaltitle(self):
        return self.orgtitle

    def get_startyear(self):
        return self.startyear

    def get_runtime(self):
        return self.runtime

    def get_genre(self):
        return self.genre

    def get_rating(self):
        return self.rating

    def get_numvotes(self):
        return self.numvotes
