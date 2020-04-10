from ...val import Val


class Pair(Val):

    @classmethod
    def Pair(self, *args):
        x = self.First(*args[0:])
        y = self.First(*args[1:])

        return Val(
            Val(
                x,
            ),
            Val(
                Val(),
                y,
            ),
        )

    @classmethod
    def Left(self, *args):
        val = self.First(*args)

        if len(val) != 2:
            return Val()

        for v in val:
            if len(v) != 1:
                continue
            for ret in v:
                return ret

        return Val()

    @classmethod
    def Right(self, *args):
        val = self.First(*args)

        if len(val) != 2:
            return Val()

        for v in val:
            if len(v) != 2:
                continue
            for ret in v:
                if len(ret) == 0:
                    continue
                return ret

        return Val()
