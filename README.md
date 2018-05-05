# movie-list

The end result of extreme boredom and the sufferings after watching some really low-rated movies on TV.

This script is really helpful when you want to know the the Movies that are to be telecasted on TV
along with their `"Timing"` and `"IMDb Rating"`, so you never miss out a good watch right when you sit
on your movie-list.

This project is completed and still can be modified with several other features.


### Dependencies
-----------------

Install all the dependencies using `sudo pip install -r requirements.txt` before using the script.

   * BeautifulSoup
   * requests
   * tabulate
   * fpdf
   * lxml

### Usage
-----------------

**Run the program:**

    $ python __main__.py 
 select option 1 or 2 based on your choice 
option 1:-
    `channel name` : Name of the movie channel

option 2:-
	genre like action , comedy etc
Where the supported channels are:

- star-movies
- sony-max
- movies-now
- romedy-now
- movies-ok
- sony-pix
- hbo
- filmy
- star-gold

**Example:**

    $ python __main__.py 
 then press 1 and enter
star movies


**Output:**

    Movie: Dawn of the Planet of the Apes  Time: 21:00 - 23:45  Rating: 7.6


And it's done! You have the name of the movie, timings and most importantly, the IMDb rating for the movie
right in front of you on the Terminal.

### Features
-----------------

Currently supported:

- [x] Provides IMDb ratings for movies

**TODOs**:

- [x] Print output in `Prettytable` format
- [ ] Allow search for Entertainment Channels
- [x] Provide option to save details as PDF
- [ ] Send notification to the user

### Contribute

Have any suggestions? Please feel free to report as issues/pull requests.
