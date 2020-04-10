class Val:
    def __init__(self, *args):
        args = set(args)
        args = list(args)
        args.sort()
        self.__value = args

    def __str__(self):
        return self.__value.__str__()

    def __repr__(self):
        return self.__value.__repr__()

    def __iter__(self):
        return self.__value.__iter__()

    def __hash__(self):
        return hash(self.__repr__())

    def __len__(self):
        return len(self.__value)

    def __lt__(self, other):
        return self.__value < other.__value

    def __eq__(self, value):
        if len(self.__value) != len(value.__value):
            return False

        for x, y in zip(self.__value, value.__value):
            if x != y:
                return False

        return True

    @classmethod
    def Empty(self, *args):
        return Val()

    @classmethod
    def First(self, *args):
        if len(args) == 0:
            return Val()
        return args[0]

    @classmethod
    def Union(self, *args):
        args = [val for arg in args for val in arg]
        return Val(*args)

    @classmethod
    def Intersection(self, *args):
        x = self.First(*args[0:])
        y = self.First(*args[1:])

        if len(args[2:]) == 0:
            args = [val for val in x if val in y]
            return Val(*args)

        ret = self.Intersection(x, y)
        return self.Intersection(ret, *args[2:])

    @classmethod
    def Complement(self, *args):
        x = self.First(*args[0:])
        y = self.First(*args[1:])
        args = [val for val in x if val not in y]
        return Val(*args)

    @classmethod
    def Append(self, *args):
        x = self.First(*args)
        return Val(*x, *args[1:])

    @classmethod
    def Remove(self, *args):
        x = self.First(*args)
        args = [val for val in x if val not in args[1:]]
        return Val(*args)
