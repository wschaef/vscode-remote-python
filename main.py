import matplotlib.pyplot as plt

a = 3+4;

print(a);

def func(a,b):
    print('a+b=',a+b);

func(3,12); 

func(3.5,8.5);     

plt.plot([1,2,3,4],[1,4,9,16],'ro');
plt.show();