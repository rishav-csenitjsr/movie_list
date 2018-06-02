# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import fpdf
import string
from itertools import islice

'''
   Currently supports:  #star-movies
            #sony-max
            #movies-now
            #romedy-now
            #movies-ok
            #sony-pix
            #hbo
            #filmy
            #star-gold
'''

web_url = "http://tvinfo.in/"
web_url2= "http://tvscheduleindia.com/channel/"
web_url3="http://tvscheduleindia.com"
base_url = 'http://www.imdb.com/find?q='


movie_name =[]
movie_time=[]
movie_rating=[]
movie_channel=[]
movie_date=[]
movie_dur=[]
movie_genre=[]

def get_rating(self ):
        try:
            print "Checking IMDb rating of "+ self.movie_name
            movie_search = '+'.join(self.movie_name.split())
            movie_url = base_url + movie_search + '&s=all'
            print(movie_url)
            br = Browser()
            br.open(movie_url)
            link = br.find_link(url_regex=re.compile(r'/title/tt.*'))
            res = br.follow_link(link)
            soup = BeautifulSoup(res.read(), "lxml")
            movie_title = soup.find('title').contents[0]
            rate = soup.find('span', itemprop='ratingValue')
            if rate is not None:
                self.movie_rating=rate

        except:
            self.movie_rating='-'

movies_of_my_genre=[]



#Method to initialize pdf object
def pdf_save(data_movies,headers):
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Tv Timings !",ln=1, align="C")
    #pdf.cell(200, 10, str(tabulate(data_movies,headers)),0,1, align="l")
    for data in data_movies:
        str1 = "Movie: " + str(data[0]) + "      Time: " + str(data[1]) + "      Genre: " + str(data[2]) + "      Rating: " + str(data[4])
        pdf.cell(200, 10, str1,0,1, align="M")
    pdf.output('list.pdf')

def getBSoup(url):
    print'''
Processing...

    '''
   # req = urllib2.urlopen(url)
    hi=requests.get(url)
    soup = BeautifulSoup(hi.content, "lxml")
    return soup


def search_channel(channel2):
    time = []
    ratings = []
    channel2_url = web_url2 + channel2
    soup2 = getBSoup(channel2_url)
   # print soup2
    s= soup2.find('tbody')
       # print s
    count=0
    for items in s.find_all("tr"):
        #print items
        if count==4 : continue
        a= items.contents[1].text
        a=a.encode('utf-8')
        b= items.contents[2].text
        b = " - ".join([item.strip() for item in b.split("-")])
        #print b
        c= items.contents[3].text
        d= items.contents[4].text
        movie_name.append(a)
        movie_time.append(b)
        movie_genre.append(c)
        movie_dur.append(d)
        count=count+1


   
    for i in range(0, len(movie_name)):
        try:
            print "Checking IMDb rating of " + movie_name[i]
            movie_search = '+'.join(movie_name[i].split())
            #movie_url = base_url + movie_search + '&s=all'
            movie_url = base_url + movie_search
            #print movie_url
            hi=requests.get(movie_url)
            soup = BeautifulSoup(hi.content, "lxml")
            xx=soup.find('tr',{"class","findResult odd"})
            #print xx
            out= xx.find('a', href=True)['href']
            #print out
            hi=requests.get("http://www.imdb.com"+out)
            soup = BeautifulSoup(hi.content, "lxml")
            rate = soup.find('span', itemprop='ratingValue')
            #print rate
            if rate is not None:
                movie_rating.append(rate.text)
            else:
                movie_rating.append("-")
        except:
            movie_rating.append("-")
        print movie_rating
        

    headers = ['Movies', 'Time', 'Genre','Duration','Rating']
    data_movies = []
    for i in range(0, len(movie_name)):
        data_movies.append([str(movie_name[i]), str(movie_time[i]),str(movie_genre[i]),str(movie_dur[i]),str(movie_rating[i])])
    print tabulate(data_movies, headers=headers)

    # Saving to pdf

    print("\nWant to save as pdf? Y/N")
    choice = raw_input().lower()
    if choice == 'y':
        pdf_save(data_movies, headers)
        print('\nSaved!')
    else:
        print('\nBye!')

def genre_recommend(genre,no_of_channel):
    genre=genre.lower()
    genre=genre.title()
    soup3=getBSoup(web_url3)
    soup4=soup3.find_all('div',{'class' : 'row' })[1]
    #print soup4
    for row in islice(soup4.find_all('a'),int(no_of_channel)): 
        #print row    
                            # This decides how many channels to see (here 10)
        channel_name= row.find('span').text.replace('\n','')
        print 'Searching in  :' + channel_name
        soup5=getBSoup(web_url3 + row.get('href'))
        s= soup5.find('tbody')
        #print s
        for items in s.find_all("tr"):
              c= items.contents[3].text
              if(c==genre):
                a= items.contents[1].text
                a=a.encode('utf-8')
                print a
                b= items.contents[2].text
                b = " - ".join([item.strip() for item in b.split("-")])
                print b
                c= items.contents[3].text
                print c
                d= items.contents[4].text
                print d


        


def main():

    print'''
                              Welcome to Movie Info !!!!                                           
    '''
    print("If you want to check movies on a channel select 1")
    print("To get movies of a specific Genre select 2")
    choice=raw_input("Enter choice: ")

    if(str(choice)=='1'):
        channel2 = raw_input("Enter name of the TV Channel: ")
        if(len(channel2.split())>1):
            channel2 = "-".join([item.strip() for item in channel2.split(" ")])
            channel2 = channel2.title()
        else:
            channel2 = channel2.strip()
            channel2 = channel2.title()
        movie_rating = search_channel(channel2)
    else:
        genre = raw_input("Enter Genre: (like  comedy, action ....) ")
        no_of_channel = raw_input("Enter No of channels to check (e.g, 1-44)")
        genre_recommend(genre, no_of_channel)
        '''
        print '\nNumber of movies of genre ' + genre.upper()+' found : ' + str(len(movies_of_my_genre))
        get_ratings(movies_of_my_genre)
        sorted_list = sorted(movies_of_my_genre, key=lambda movie: movie.movie_rating, reverse=True)

        headers = ['Movies','Channel','Time', 'Rating']
        data_movies2 = []

        for movie in islice(sorted_list, 5):
            data_movies2.append([movie.movie_name.replace('\t', ''), movie.movie_channel.replace('\t', ''), movie.movie_start+"-"+movie.movie_end, movie.movie_rating])
        print tabulate(data_movies2, headers=headers)
        '''


if __name__ == '__main__':
    main()
