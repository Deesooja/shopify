import threading
import time

class CreateTheads(threading.Thread):
    
    def __init__(self,target_fun,args=None):
        super().__init__()
        self.target_fun =target_fun
        self.args=args

    def run(self):
        if self.args:
            self.target_fun( args for args in self.args)
        else:
            self.target_fun()



def create(count):
    time.sleep(2)
    print('created',count)


def createCronJob():
    for i in range(5):
        create(i)


def update(count):
    time.sleep(2)
    print('update',count)


def updateCronJob():
    for i in range(5):
        update(i)     

# crete_thead_list=[]
# update_thead_list=[]

# def create(count):
#     time.sleep(2)
#     print('created',count)


# def createCronJob():
#     for i in range(5):
#         create_thead=threading.Thread(target=create,args=[i])
#         create_thead.daemon=True
#         create_thead.start()
#         crete_thead_list.append(create_thead)
        
#     for crate_tread in crete_thead_list:
#         crate_tread.join()



# def updated(count):
#     time.sleep(2)
#     print('Updated',count)

# def updateCronJob():
#     for i in range(5):
#         update_thead=threading.Thread(target=updated,args=[i])
#         update_thead.daemon=True
#         update_thead.start()
#         update_thead_list.append(update_thead)

#     for update_thead in update_thead_list:
#         update_thead.join()