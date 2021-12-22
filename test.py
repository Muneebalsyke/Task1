import csv

with open('movies_dataset.csv', 'r') as Movies1:
    MoviesList = csv.reader(Movies1)
    Movies_Data = list(MoviesList)
print(Movies_Data)
print(Movies_Data[1][2])

top10 = []
print("Input the year from which you want to see top 10 movies ?")
c = input()
for p_list in Movies_Data:

    if p_list[3] == c:
        top10.append(p_list)

top10.sort(key=lambda a: a[3])

for n in top10:
    if n == 10:
        break
    print(n)

print("Please input the genre for num of Movies and rating")
z = input()
nom = 0
mr = []
for g_list in Movies_Data:

    if z in g_list[5]:
        nom += 1
        mr.append(g_list[6])
avg = 0.0
for i in mr:
    x = float(i)
    avg = avg + x
avg = avg / nom

print('Which year you want to get highest and lowest rating movie from? ')
s = input()
l = 10
h = 0
i = 0
x = []
y = []
for x_list in Movies_Data:
    # if i == 0:
    #     i = i + 1
    #     break
    # for y_list in x_list:
    # for y in enumerate(x):

    if x_list[3] == s:
        if l > float(x_list[6]):
            l = float(x_list[6])
            x = x_list
        elif h < float(x_list[6]):
            h = float(x_list[6])
            y = x_list
    sol = int(x[4]) + int(y[4])
    sol = sol / 2
    print(f"The lowest rating movie of {s} is : {x[2]}  "
          f"whereas highest is : {y[2]} ,  with average mean minutes = {sol}]")
