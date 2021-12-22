import csv

import Result as Result

import MoviesClass
import Movie_parser
import MovieList
import Result
import os

if __name__ == "__main__":
    os.environ['DB_URL'] = "movies_dataset.csv"
    dataset = os.environ.get('DB_URL')
    # for line in Movies_Data:
    #     print(line)
    # print(dataset)
    # print(type(dataset))
    with open(dataset, 'r') as Movies1:
        Movies_Data = csv.reader(Movies1)

        # for line in Movies_Data:
        #     print(line)

        MoviesList = list(Movies_Data)
    print(MoviesList)
    print(type(MoviesList))

    mv = MoviesClass.Movies(MoviesList)
    bo = True
    while bo is True:
        print("1. For a given year display the highest rating and movie name, "
              "lowest rating and movie name, and average runtime minutes? for this qs press r.  ")
        print("For a given genre display the number of movies and the mean rating? for this qs press g.  ")
        print("For a given year print the top ten highest rated movies (using numVotes). "
              "Also print a :grinning: for every x votes such that at max you can print 80 likes. for this qs press v")
        print("Press 0 to exit.")
        i = input()
        if i == '0':
            break
        Rs = Result.Result(i, MoviesList)
        Rs.result()
        if i == '0':
            break
