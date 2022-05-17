# USANDO UN PROCESO DENTRO DE UNA CLASE

import multiprocessing


class MyProcess(multiprocessing.Process):

    def run(self):
        print("Método run llamado dentro del proceso: %s" % self.name)
        return


if __name__ == '__main__':

    jobs = []
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()

