import jpype


def useJava(a, b):
    # 启动JVM
    jvmPath = jpype.getDefaultJVMPath()
    # 加载jar包
    if not (jpype.isJVMStarted()):
        jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=MathDemo.jar")
    # 指定main class
    JDClass = jpype.JClass("com.test.Main")
    # 创建类实例对象
    jd = JDClass()
    # 引用jar包类中的方法 add
    result = jd.add(a, b)
    # 关闭JVM
    # jpype.shutdownJVM()
    return result


if __name__ == '__main__':
    print(useJava(1,2))