class Recorder:

    def __init__(self):
        raise Exception("it is a singleton class. Use get_instance instead.")

    __instance = None

    @classmethod
    def get_instance(cls):
        if Recorder.__instance == None:
            Recorder.__instance = Recorder.__new__(cls)
        return Recorder.__instance

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val

if __name__ == "__main__":
    try:
        r1 = Recorder()
    except Exception:
        print("Failed to call constructor")
    r1 = Recorder.get_instance()
    r1.set_val(5)
    print(r1.get_val())

    r2 = Recorder.get_instance()
    r2.set_val(3)
    print(r2.get_val())
    print(r1.get_val())