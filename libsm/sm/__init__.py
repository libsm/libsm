import logging
from ..val import Val
from ..std.pair import Type as Pair


class SM:
    def __init__(self, fi, fn, logger=None):

        self.logger = logging.getLogger(name=logger)

        self.__V = set()
        self.__E = set()
        N = set()

        try:
            self.logger.info('[SM] [INIT] [START]')

            sns = fi()
            for v in sns:
                N.add(v)

            self.logger.info('[SM] [INIT] [DONE]')
            self.log()
            self.logger.info('[SM] [LOOP] [START]')

            while True:
                sn = N.pop()
                sns = fn(P=sn)

                self.__V.add(sn)
                for v in sns:
                    self.__E.add((sn, v))
                    if v in self.__V:
                        continue
                    N.add(v)

                self.log(sn=sn, sns=sns)
        except KeyError:
            self.logger.info('[SM] [LOOP] [DONE]')
            return

    def V(self):
        return Val(*self.__V)

    def E(self):
        ret = [Pair.Pair(x, y) for x, y in self.__E]
        return Val(*ret)

    def result(self):
        return self.__V, self.__E

    def verify(self, fv):
        V, E = self.V(), self.E()
        assert fv(V=V, E=E) == Val()

    @classmethod
    def log(self, sn=None, sns=None):
        pass
