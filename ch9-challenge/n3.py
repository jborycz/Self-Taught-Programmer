listoflists = [[" Top Gun", "Risky Business", "Minority Report"], [" Titanic", "The Revenant", "Inception"], [" Training Day", "Man on Fire", "Flight"]]

import csv

with open("listoflists.csv","w+",newline='') as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(listoflists[0])
    w.writerow(listoflists[1])
    w.writerow(listoflists[2])
