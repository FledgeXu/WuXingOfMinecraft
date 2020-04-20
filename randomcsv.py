import csv
import random

with open('./MinecraftWholeItemElements.csv') as f:
    with open("./MinecraftWholeItemElementsRandom.csv",'w') as w:
        spamwriter =  csv.writer(w,delimiter=',')
        f_csv = csv.reader(f)
        headers = next(f_csv)
        spamwriter.writerow(headers)
        for row in f_csv:
            row[1] = str(int(row[1])+random.randint(1, 11))
            row[2] = str(int(row[2])+random.randint(1, 11))
            row[3] = str(int(row[3])+random.randint(1, 11))
            row[4] = str(int(row[4])+random.randint(1, 11))
            row[5] = str(int(row[5])+random.randint(1, 11))
            spamwriter.writerow(row)
            print(row)
