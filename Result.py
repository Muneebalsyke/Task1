from emoji.core import emojize
import csv
from MoviesClass import Movies


# with open('movies_dataset.csv', 'r') as Movies1:
#     Movies_Data = csv.reader(Movies1)
#     mv = list(Movies_Data)


class Result(Movies):

    def __init__(self, string, mv):
        self.string = string
        super(Result, self).__init__(mv)
        self.movielist = mv

    def result(self):
        if self.string == 'r':
            print('Which year you want to get highest and lowest rating movie from? ')
            s = input()
            k = 10
            h = 0
            x = []
            y = []
            # if s not in range(1500, 2000):
            #     print("No Movies found")
            for x_list in self.movielist:
                # if i == 0:
                #     i = i + 1
                #     break
                # for y_list in x_list:
                # for y in enumerate(x):

                if x_list[3] == s:
                    if k > float(x_list[6]):
                        k = float(x_list[6])
                        x = x_list
                    elif h < float(x_list[6]):
                        h = float(x_list[6])
                        y = x_list
            try:
                print(f"The lowest rating movie of year {s} is : {x[2]}  "
                      f"whereas highest is : {y[2]} ,  with average mean minutes = {x[4]} and {y[4]} respectively")
            except:
                print("No Movies found")
                pass

            if len(x) and len(y) == 0:
                print("No Movies found")

        elif self.string == 'g':
            print("Please input the genre for num of Movies and rating")
            z = input()
            nom = 0
            mr = []
            for g_list in self.movielist:

                if z in g_list[5]:
                    nom += 1
                    mr.append(g_list[6])
            avg = 0.0
            for i in mr:
                x = float(i)
                avg = avg + x
            avg = avg / nom
            print(f"Total movies found for genre {z} amount to {nom} with Average Mean Rating of {avg}")

            if len(mr) == 0:
                print("No movies found")

        elif self.string == 'v':
            top10 = []
            m = 0
            print("Input the year from which you want to see top 10 movies ?")
            c = input()
            for p_list in self.movielist:

                if p_list[3] == c:
                    top10.append(p_list)

            top10.sort(key=lambda a: a[3])

            for n in top10:
                if n == 10:
                    break
                print(n)
                m = int(n[7])
                m = m // 80
            for m in range(1, m):
                print(emojize(":smiling_face_with_sunglasses:"))
            if len(top10) == 0:
                print("No Movies Found")

        else:
            print("No Movies found.")
