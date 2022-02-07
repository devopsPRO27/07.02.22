from Address import *

class User:
    def __init__(self,d):
        self.__dict__=d
        currentadd=Address(self.address)
        self.address=currentadd   #obj.dic= obj(dic)

    def __str__(self):
        result=""
        for k,v in self.__dict__.items():
            if k=='address':
                result+=self.address.__str__()
            result+=f'{k} ={(str)(v)} \n'
        return result


def main():
    print('hii')
    print('hii')
    print('hii')
    print('hii')

if __name__=='__main__':
    main()


