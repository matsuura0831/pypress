
class Hoge(object):
    def __init__(self, value):
        self._value = value

    def fuga(self):
        return self._value

def main():
    print(Hoge(10).fuga())