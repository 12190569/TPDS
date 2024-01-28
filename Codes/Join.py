import glob
import os
for f in glob.glob("*.csv"):
    os.system("cat "+f+" >> Ano.csv")
