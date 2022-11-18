import pandas as pd
import matplotlib.pyplot as plt

#read csv files using pandas library 
anonym_views = pd.read_csv("anonymized_viewings.csv")
metadata = pd.read_csv("metadata.csv")


content = pd.merge(anonym_views,metadata) #joined 2 csv files by content_id 


summ_content = 0


# content["title"].value_counts() --> counts each title how many times occurred in dataset 
df = pd.DataFrame(content["title"].value_counts())
df.to_csv("/Users/asselbatu/Desktop/Task/title_per.csv")

for val in content["title"].value_counts():

	summ_content += val   #sum of all titles appeared in dataset

#print(summ_content)

#summ_content --> 100%
#val --> ?

arr = []
count_all = 0
count_big_titles = 0
count_small_titles = 0
for val in content["title"].value_counts():
	count_all += 1
	
	percent_each_title = format(((val*100)/summ_content),'.2f')
	if float(percent_each_title) > 1:

		count_big_titles += 1
	else:
		count_small_titles += 1

	arr.append(percent_each_title)

#Big Titles
#count_all --> 100
#count_big_titles, count_small_titles --> ?

count_big_titles = format(((count_big_titles*100)/ count_all),'.2f')
count_small_titles = format(((count_small_titles*100)/ count_all),'.2f')
print(count_big_titles)
print(count_small_titles)

df.insert(1,"%",arr) 
df.to_csv("/Users/asselbatu/Desktop/Task/title_per.csv")




#GENRES
df = pd.DataFrame(content["genres"].value_counts())
df.to_csv("/Users/asselbatu/Desktop/Task/genres.csv")

summ_genres = 0
for val in content["genres"].value_counts():

	summ_genres += val 	

arrg = []
for val in content["genres"].value_counts():
	
	percent_each_genres = format(((val*100)/summ_genres),'.2f')
	
	arrg.append(percent_each_genres)

df.insert(1,"%",arrg) 
df.to_csv("/Users/asselbatu/Desktop/Task/genres.csv")

