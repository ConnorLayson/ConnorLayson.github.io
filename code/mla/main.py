from js import document

global italics
global bold

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

def mainMenu():
    global selection
    print(bold +'--==MLA Citation Generator==--')
    print(blue + 'Made by Connor Layson 2021' + end)
    print()
    print('To use:')
    print('Select menu options by typing the number ')
    print('corresponding with the option you want to select.')
    print('When prompted, type information. ' + bold + underline + 'DO NOT' + end + ' put punctuation')
    print(italics + 'Note: When prompted with DD/MMM/YYYY, DD is the day, MMM')
    print('is where you abreviate the month, and YYYY is the year.' + end)
    print()
    print('Enter the type of source you are using today:')
    print('1) Book')
    print('2) Website')
    print('3) Magazine')
    print('4) Newspaper')
    print('5) A review')
    print('6) Editorial')
    print('7) Letter')
    print('8) Anonymous articles')
    print('9) Scholarly jornal article')
    print('10) Interviews')
    print('11) Oral presentation (Speeches, Lectures, etc.)')
    prosessInput()

def prosessInput():
    selection = document.getElementById('command').value
    print('You have selected ' + selection + '.')
    print()
    print('Now Loading...')
    print()
    if selection == '1':
        book()
    elif selection == '2':
        web()
    elif selection == '3':
        mag()
    elif selection == '4':
        newspaper()
    elif selection == '5':
        review()
    elif selection == '6':
        edit()
    elif selection == '7':
        letter()
    elif selection == '8':
        anonArtic()
    elif selection == '9':
        scholJorn()
    elif selection == '10':
        inter()
    elif selection == '11':
        oralPres()
    else:
        print('Invalad selection or error prossesing your selection')
        print('Please try again')
        print('Error code: 001')
        print()
        print('Restarting...')
        print()
        mainMenu()

def book():
    print('Now formating for: Book')
    print()
    firstname = input("Author's First name: ")
    lastname = input("Author's Last name: ")
    title = input("Title of book: ")
    publish = input("Publisher: ")
    publishDate = input("Publication Date (YYYY): ")
    print()
    print('Now generating your MLA citation...')
    print()
    print(lastname + ', ' + firstname + '. ' + italics + title + end + '. ' + publish + ', ' + publishDate + '.')

def web():
    print('Now formating for: Website')
    print()
    sitename = input("Website name: ")
    affiliation = input("Organization Affiliated with the website(What company and/or organization is this website for?): ")
    date = input("Creation date (YYYY): ")
    url = input("URL of " + bold + "HOME " + end + "page of the website (Not the https:// part): ")
    accessed = input("Date you accesed the site (DD/MMM/YYYY): ")
    print()
    print('Now generating your MLA citation...')
    print()
    print(italics + sitename + end +'. ' + affiliation + ', ' + date + ', ' + url + '. Accessed ' + accessed + '.')

def mag():
    print('Now formating for: Magazine')
    print()
    firstname = input("Author's first name: ")
    lastname = input("Author's last name: ")
    title = input ('Title of the article: ')
    magTitle = input('Title of Magazine: ')
    date = input('Publication date (DD/MMM/YYYY): ')
    startPage = input('Starting page: ')
    endPage = input('Ending page: ')
    print()
    print('Now generating your MLA citation...')
    print()
    print(lastname + ', ' + firstname + '. "' + title + '." ' + italics + magTitle + end +', ' + date + ', pp. ' + startPage + '-' + endPage + '.')

def newspaper():
    print('Now formating for: Newspaper')
    print()
    firstname = input("Author's first name: ")
    lastname = input("Author's last name: ")
    title = input ('Title of the article: ')
    magTitle = input('Title of Newspaper: ')
    date = input('Publication date (DD/MMM/YYYY): ')
    startPage = input('Page: ')
    print()
    print('Now generating your MLA citation...')
    print()
    print(lastname + ', ' + firstname + '. "' + title + '." ' + italics + magTitle + end + ', ' + date + ', p. ' + startPage + '.')

def review():
    print('Now formating for: A review')
    print()
    firstname = input('First name of who wrote the review: ')
    lastname = input('Last name of who wrote the review: ')
    title = input('Review title (If there is none, just press Enter): ')
    prefTitle = input('Preformance title (title of the thing being reviewed): ')
    person = input('Director/Author/Artist name: ')
    role = input('Role of the person in the previous reponse (edited, directed, ect.): ')
    workTitle = input('Place the review was in (ex: The New York Times): ')
    date = input('Date it was created (DD/MMM/YYYY): ')
    page = input('Page number the review was on: ')
    print()
    print('Now generating your MLA citation...')
    print()
    print(lastname + ', ' + firstname + '. "' + title + '." Review of ' + italics + prefTitle + end +', ' + role + ' by ' + person + '. ' + italics + workTitle + end + ', ' + date + ', p. ' + page + '.')

def edit():
    print('Now formating for: An editorial')
    print()
    first = input('Title (in qotations) ' + bold + 'OR ' + end + 'author name (last, first): ')
    title = input('Title of publishing company: ')
    date = input('Publish date (DD/MMM/YYYY): ')
    page = input('Page: ')
    print()
    print('Now generating your MLA citation...')
    print()
    print(first + '. Editorial. ' + italics + title + end + ', ' + date + ', p. ' + page + '.')

def letter():
    print('Now formating for: A letter')
    print()
    first = input('Title (in qotations) ' + bold + 'OR ' + end + 'author name (last, first): ')
    title = input('Title of publishing company: ')
    date = input('Publish date (DD/MMM/YYYY): ')
    page = input('Page: ')
    print()
    print('Now generating your MLA citation...')
    print()
    print(first + '. Letter. ' + italics + title + end + ', ' + date + ', p. ' + page + '.')

def anonArtic():
    print('Now formating for: An Anonymous Article')
    print()
    title = input('Title of article: ')
    otherTitle = input('What was the article writen in(ex: New York Times): ')
    date = input('Date it was written (DD/MMM/YYYY): ')
    page = input('Page the article was on: ')
    print()
    print('Now generating your MLA citation...')
    print()
    print('"' + title + '." ' + otherTitle + ', ' + date + ', p. ' + page + '.')

def scholJorn():
    print('Now formating for: A Scholarly Jornal')
    print()
    firstname = input('First name of the author: ')
    lastname = input('Last name of the author: ')
    title = input('Article title: ')
    jornal = input('Jornal title: ')
    volume = input('Volume number: ')
    issue = input('Issue number: ')
    year = input('Year it was written: ')
    page_start = input('Starting page: ')
    page_end = input('Ending Page: ')
    print()
    print('Now generating your MLA citation...')
    print()
    print(lastname + ', ' + firstname + '. "' + title + '." ' + italics + jornal + end + ', vol. ' + volume + ', no. ' + issue + ', ' + year + ', pp. ' + page_start + '-' + page_end + '.')

def inter():
    print('Now formating for: Interviews')
    print()
    firstname = input("Interviewer's first name: ")
    lastname = input("Interviewer's last name: ")
    interviewed = input('The name of the person being interviewed: ')
    container = input('What was the interview writen in (ex. New York Times): ')
    print(italics + 'Note: For the next few questions, if there is none, just press "Enter"')
    print('and exempt that portion from the final copy.' + end)
    volume = input('Volume: ')
    issue = input('Issue: ')
    startpage = input('Starting page: ')
    endpage = input('Ending page: ')
    print()
    print('Now generating your MLA citation...')
    print()
    print(lastname + ', ' + firstname + '. Interview with ' + interviewed + '. ' + italics + container + end + ', vol. ' + volume + ', no. ' + issue + ', ' + year + ', pp. ' + startpage + '-' + endpage + '.')

def oralPres():
    print('Now formating for: Oral Presentations')
    print()
    firstname = input("Speaker's first name: ")
    lastname = input("Speaker's last name: ")
    title = input('Speech title (If none, press enter): ')
    name = input('Confrance name (Name of the confrance it was presented for):')
    date = input('Date it was presented (DD/MMM/YYYY): ')
    address = input('Address of the location it was presented in: ')
    print()
    print('Now generating your MLA citation...')
    print()
    print(lastname + ', ' + firstname + '. "' + title + '." ' + name + ', ' + date)

mainMenu()
