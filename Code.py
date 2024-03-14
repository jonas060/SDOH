import subprocess
import sys
import pandas

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#install("pandas")



