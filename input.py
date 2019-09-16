import sys
import getopt
import testJava

def getiput(argv):
    a = ""
    b = ""
    try:
        opts, args = getopt.getopt(argv, "a:b:")
    except getopt.GetoptError:
        print('usage: python input.py -a a -b b')
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-a"):
            a = arg
        else:
            b = arg
    print('a:', a)
    print('b:', b)
    a,b = int(a), int(b)
    print(testJava.useJava(a,b))
    '''
    for i in range(0, len(args)):
        print('参数 %s 为：%s' % (i + 1, args[i]))
    '''


if __name__ == '__main__':
    getiput(sys.argv[1:])

