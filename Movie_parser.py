# import csv
# import os
# from MoviesClass import Movies
#
# os.environ['mv_data'] = "movies_dataset.csv"
# dataset = os.environ.get('mv_data')
# print(dataset, type(dataset))
# with open('movies_dataset.csv', 'r') as Movies1:
#     Movies_Data = csv.reader(Movies1)
#
#     # for line in Movies_Data:
#     #     print(line)
#
#     MoviesList = list(Movies_Data)
#     # print(MoviesList)
#
# mv = Movies(MoviesList[1])
# mv.movie_parser(MoviesList[1])
# c = mv.get_id()
# print(c)