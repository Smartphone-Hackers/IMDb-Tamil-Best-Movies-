import requests
from bs4 import BeautifulSoup

year = input("Enter Year : ")

url = 'https://www.imdb.com/search/title?explore=languages&title_type=feature&year={0},{0}&languages=ta&sort=moviemeter,asc&ref_=adv_explore_rhs'.format(year)

source = requests.get(url).content

soup = BeautifulSoup(source,'lxml')

div_tag = soup.find_all('div',{"class":"lister-item mode-advanced"})

movies_name_rate = {} 

for img in div_tag:
	name = img.find('img').get('alt')
	rate = img.find('strong')

	if rate == None:
		movies_name_rate[name] = 'No Rating'
	else:
		movies_name_rate[name] = rate.text

print("All Movies List With Rating : Press 1")
print("Above 8.0 Rating Movies Only : press 2")

try:
	Number = int(input("Enter Number  : "))
except:
	print("Please Enter Number Only")

size = []
for i in movies_name_rate:
	size.append(len(i))

#All Movies Rating:-
def all_movie_with_rating():
	for i in movies_name_rate:
		space = movies_name_rate[str(i)].replace(' ','')
		if space.isalpha():
			pass
		else:
			print(i,' '*(max(size)-len(i)),':',' '*10,movies_name_rate[i])

#Above n Rating Movies Only:-
def particular_rating_movies():
		for i in movies_name_rate:
			space = movies_name_rate[str(i)].replace(' ','')

			if space.isalpha():
				pass	
			else:
				if type(float(movies_name_rate[i])) == float or type(int(movies_name_rate[i])) == int:
					if float(movies_name_rate[i]) >= 8.0:
						print(i,' '*(max(size)-len(i)),':',' '*10,movies_name_rate[i])

if Number == 1:
	all_movie_with_rating()
elif Number == 2:
	particular_rating_movies()
