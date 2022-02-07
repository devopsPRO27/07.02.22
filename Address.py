class Address:
    def __init__(self,d):
        self.__dict__=d

    def __str__(self):
        result='Address\n'
        for k,v in self.__dict__.items():
            result+=f'{k }= {str(v)} \n'
        return result
