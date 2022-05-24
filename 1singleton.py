class Recorder:
    class __Recorder:
        def __init__(self):
            self.val = None

        # def __str__(self):
        #     return ("{0!r}".format(self))

        def get_val(self):
            return self.val

    __instance = None

    def __new__(cls, *args, **kwargs):
        if Recorder.__instance == None:
            Recorder.__instance = Recorder.__Recorder()
        return Recorder.__instance

    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)

    def __str__(self):
         return str(self.__instance)

if __name__ == "__main__":
    r1 = Recorder()
    r1.val = 5
    print(r1, r1.get_val())

    r2 = Recorder()
    print(r2, r2.get_val())
    print(r1 is r2)