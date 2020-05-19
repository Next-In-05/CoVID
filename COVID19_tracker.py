# Author : Next In

print('Author : Next Innovation\n')
print('Please Connect Device with Internet\n')
print('Connecting To Ministry Of Health....\n\n')

from requests import get
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from matplotlib import pyplot as plt

url = 'https://www.mohfw.gov.in/'
web_content = get(url).content
print('Data succesfully fetch by Ministry of Health India\n\n\n')
soup = BeautifulSoup(web_content , "html.parser")
extract_contents = lambda row: [x.text.replace('\n','')for x in row]
stats = []
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    if len(stat) == 5:
        stats.append(stat)
new_column = ['Sr.no.' , 'States/UT' , 'Confirmed' , 'Recovered' , 'Death']
name =[]
confirm = []
recover = []
death = []
del(stats[len(stats)-1])
for x in stats:
    name.append(x[1])
    confirm.append(int(x[2]))
    recover.append(int(x[3]))
    death.append(int(x[4]))
table = PrettyTable()
table.field_names = (new_column)

for i in stats:
    table.add_row(i)
table.add_row(["","Total", 
               sum(confirm), 
               sum(recover), 
               sum(death)])
print(table)
plt.figure(figsize = (15,10))
plt.barh(name,confirm,align = 'center',color='lightblue',edgecolor='blue',label='Author : Next Innovation')
plt.title('Total Confirmed Case StateWise',fontsize = 18)
plt.xlabel('No. of Confirmed cases',fontsize = 18)
plt.ylabel('States/UT',fontsize = 18)
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 7)
for index, value in enumerate(confirm):
    plt.text(value, index, str(value), fontsize = 8)
plt.legend()

c=(sum(confirm))
r=(sum(recover))
d=(sum(death))
re=(sum(confirm)-sum(recover))

plt.figure(figsize = (15,10))
plt.barh(name,recover,align = 'center',color='lightblue',edgecolor='brown',label = 'Next Innovation')
plt.title('Total Recovered Case StateWise',fontsize = 18)
plt.xlabel('No. of Recovered cases',fontsize = 18)
plt.ylabel('States/UT',fontsize = 18)
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 7)

for index, value in enumerate(recover):
    plt.text(value, index, str(value), fontsize = 8)
plt.legend()

group_size = [c,r,d,re]
group_labels = ['Confirmed\n' + str(c), 
                'Recovered\n' + str(r), 
                'Death\n'  + str(d) +'\n\n Next Innovation',
                'Total Active Cases\n' +str(re)]
custom_colors = ['skyblue','yellowgreen','tomato','orange']
plt.figure(figsize = (5,5))
plt.pie(group_size, labels = group_labels, colors = custom_colors, startangle=60 ,explode=(0,0.1,0.1,0.5))
central_circle = plt.Circle((0,0),0.5, color = 'white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size = 12) 
plt.title('Nationwide total Confirmed, Recovered and Deceased Cases', fontsize = 16)
plt.show()
