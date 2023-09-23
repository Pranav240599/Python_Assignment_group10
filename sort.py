class sort:

  def _init_(self, items):
      self._items = items
  
  @abstractmethod
  def _sort(self):
    pass

  def get_items(self):
    return self._items

  def _time(self):
    self.time = 0
    return self.time
class Buble_Sort(sort):

  def sort(a):
    for j in range(len(a)):
      for i in range(len(a)-1):
        if a[i]>a[i+1]:
          a[i],a[i+1]=a[i+1],a[i]
    print(a)

a=int(input("Enter the size of the list:"))
print("Enter the list:")
b=[]
for i in range(a):
  b.append(int(input()))
buble_sort(b)