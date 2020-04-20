import csv
import string
with open("./MinecraftWholeItemElementsRandom.csv", "r") as f:
    csv_fs = csv.reader(f)
    headers = next(csv_fs)
    for row in csv_fs:
        line = "spiritEnergyCollectionMap.put(Items.{}, new SpiritEnergyCollection({}F,{}F,{}F,{}F,{}F));".format(
                string.upper(row[0]),
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                )
        print(line)
