import threading
import myServer4test
thread1=threading.Thread(target=myServer4test.ConfigServer,args=())
thread2=threading.Thread(target=myServer4test.DataServer,args=())
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("所有服务器均退出")