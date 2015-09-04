import Queue
class queue(object):
	def __init__(self):pass
		#self.myque=Queue.Queue(50)
	def enqueue(self,w):
		if self.isInteger(w):
			return False
		elif self.myque.full():
			return False
		else:
			self.myque.put(w)
	def dequeue(self):
		if self.myque.empty():
			return False
		else:
			return self.myque.get()
	def isInteger(self,x):
		return type(x)!=type(5)


a = queue()
a.myque = Queue.Queue(20)
a.enqueue(1)
a.enqueue(2)
a.enqueue(5)
a.enqueue(19)
a.enqueue(11)
a.enqueue(71)
a.enqueue(56)
a.enqueue(38)
a.enqueue(22)
a.enqueue(62)
i=0
while i<10:
    print a.dequeue()
    i=i+1
