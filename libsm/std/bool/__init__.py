from ...val import Val


class Bool(Val):

    @classmethod
    def T(self, *args):
        return Val(Val())

    @classmethod
    def F(self, *args):
        return Val()

    @classmethod
    def Bool(self, *args):
        val = self.First(*args)

        if len(val) == 0:
            return self.F()

        return self.T()

    @classmethod
    def And(self, *args):
        for val in args:
            if len(val) == 0:
                return self.F()

        return self.T()

    @classmethod
    def Or(self, *args):
        for val in args:
            if len(val) > 0:
                return self.T()

        return self.F()

    @classmethod
    def Not(self, *args):
        ret = self.Bool(*args)
        return self.Equal(ret, self.F())

    @classmethod
    def Equal(self, *args):
        x = self.First(*args[0:])
        y = self.First(*args[1:])

        if x == y:
            return self.T()

        return self.F()

    @classmethod
    def Subset(self, *args):
        x = self.First(*args[0:])
        y = self.First(*args[1:])

        x = self.Union(x, y)

        if x == y:
            return self.T()

        return self.F()
