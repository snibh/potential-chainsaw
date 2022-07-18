import matplotlib .pyplot as plt
import psutil as p

name_list = []
percent_list = []

count = 0

for process in p.process_iter():
    count=count + 1
    if count <= 10:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('name ',name ,' cpu_usage' , cpu_usage)
        name_list.append(name)
        percent_list.append(cpu_usage)
        
plt.figure(figsize=(15,7))
plt.xlabel("Application")
plt.ylabel("Usage") 
plt.bar(name_list,percent_list,width=0.6,color=("red","orange","green","brown","black","yellow","blue","grey","coral","purple"))       
plt.show()