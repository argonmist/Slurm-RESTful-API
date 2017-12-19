import pyslurm
import os
def main():
    ver_report = open('/home/slurm/todo-api/logs/tmp', 'a')
    ver_report.write(str("PySLURM\t%s" % (pyslurm.version())) + '\n' + str("SLURM\t%s-%s-%s\n" % (pyslurm.slurm_api_version())))
    ver_report.close()

if __name__ == "__main__":
    main()

