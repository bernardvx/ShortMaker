import numpy as np
import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt


conn = psycopg2.connect(
    host='localhost',
    database='youtube_shorts',
    user = 'postgres',
    password='mackintosh')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS data_averaged (
id bigserial PRIMARY KEY,
view_interval varchar,
title_characters int8,
title_hashtags int8,
views int8,
length int8,
days_since_publication int8);
""")

conn.commit()

view_intervals = [0, 10000, 50000, 100000, 500000, 1000000, 5000000, 50000000, 500000000]

def select_database(a,b):
    cur = conn.cursor()
    view_intervals = [0, 10000, 50000, 100000, 500000, 1000000, 5000000, 50000000, 500000000]
    select = f"""
        SELECT id, length, views, published, title 
        FROM data where length<61 and views>{view_intervals[a]} and views <{view_intervals[b]};
        """
    cur.execute(select)
    rows = cur.fetchall()
    cur.close()
    return rows

def days_since_publication(row):
    try:
        timestamp = '2023-09-05 00:00:00'
        public_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') - datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
        time_difference = str(public_time).split(" ")[0]
    except Exception:
        time_difference = 0
    return int(time_difference)

def title_char(row):
    title_char = len(row[4])
    return title_char

def title_hash(row):
    title_hash = row[4].count('#')
    return title_hash

def average_group(group):
    groupies = np.array(group)
    mean = np.mean(groupies, axis=0)
    group_average = [f"{x:.0f}" for x in mean]
    return group_average

a,b = 0,1
group = []

value_group = []
while b<=8:
    while True:
        view_group = f"{view_intervals[a]/1000000}M-{view_intervals[b]/1000000}M" if view_intervals[a]//1000000 else f"{view_intervals[a]/1000}-{view_intervals[b]/1000}k"
        rows = select_database(a,b)
        for row in rows:
            row = [title_char(row), title_hash(row), days_since_publication(row), row[1], row[2]]
            #print("title char, title_hashtags,  days since pub, vid lenght , views<10K")
            group.append(row)
        group_average = average_group (group)
        insert = ("INSERT INTO data_averaged (view_interval ,title_characters ,title_hashtags ,views ,length ,days_since_publication ) VALUES (%s, %s,%s, %s, %s,%s);")  
        values = (view_group, group_average[0], group_average[1], group_average[4], group_average[3], group_average[2]) 
        value_group.append(list(values))
        #cur.execute(insert, values)
        #conn.commit()
        a +=1
        b+= 1
        group = []
        break
    #print(list[values])

cur.close()
conn.close()

print(value_group)
def chart_values(value_group):
    category = []
    tit_char = []
    tit_hash = []  
    leng = []
    dsp = []
    for i in value_group:
        print(i)
        category.append(i[0])
        tit_char.append(i[1])
        tit_hash.append(i[2])
        leng.append(i[4])
        dsp.append(i[5])
    return category, tit_char , tit_hash , leng, dsp 

category, tit_char , tit_hash , leng, dsp = chart_values(value_group)


plt.bar(category, dsp)
plt.xlabel('view interval')
plt.ylabel('values')
plt.title('Average days since publication  average')
plt.show()


