#!/usr/bin/python
import sys


class MgFilar:
    def analyze(self, path):
        raise NotImplementedError("Esto es una clase abstracta!")


class EurovideoMgFilar(MgFilar):
    def analyze(self, path):
        f = open(path, 'r')
        max_chars = 12
        contador = 1
        result = []
        for line in f:
            cuantos = line.count('|')
            if cuantos < max_chars:
                data = {'line': contador, 'cuantos': cuantos}
                result.append(data)
            contador += 1
        f.close()
        return result


if __name__ == "__main__":
    analizador = EurovideoMgFilar()
    result = analizador.analyze(sys.argv[1])
    print result