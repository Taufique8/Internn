#matplotlib
x = ['Taufique','Fiza','Nikku']
y = [30,50,60]
z = [15,25,30]
width=0.1
p = np.arange(len(x))
p1 = [j + width for j in p]
#colors = ['red','yellow','pink']
plt.bar(p,z,color='yellow',label='Taufique1')
plt.bar(p1,y,color='r',label='Taufique')

#plt.grid()

plt.xlabel('Name')
plt.ylabel('Number')
plt.title("Bar chart")
plt.xticks(rotation=45)
#align="edge",edgecolor='black',linewidth=2,linestyle=":",alpha=0.7,,,label='Taufique

plt.legend()
plt.show()
