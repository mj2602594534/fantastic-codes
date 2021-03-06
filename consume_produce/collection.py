from threading import Condition

from consume_produce.consumer import ConsumerThread
from consume_produce.goods import Kiwi
from consume_produce.producer import ProducerThread

if __name__=="__main__":
    kiwi=Kiwi()
    conn=Condition()



    for j in range(1,2):  # 一个消费者
        consumer=ConsumerThread("消费者"+str(j),kiwi,conn)
        consumer.start()

    for i in range(2):  # 两个生产者
        pro = ProducerThread("生产者" + str(i), kiwi, conn)
        pro.start()