import os
import subprocess
import sys
def main():
    cmd = "sbatch " + sys.argv[1]
    subprocess.call(cmd.split())

if __name__ == "__main__":
    main()

