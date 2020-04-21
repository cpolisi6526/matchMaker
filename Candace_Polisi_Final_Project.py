from pylab import*
from IPython import get_ipython
get_ipython().magic('reset -sf') 
# =============================================================================
# Candace Polisi
# Final Project: 

# =============================================================================
##when the response isnt in check
def mis():
    import random
    responses= ['Hey Im sorry I think we are misunderstanding one another. Lets just rewind', 'Mmm I was looking for a different answer Ill ask again.']
    x= random.randint(0,1)
    print(responses[x])

#it was easier to breakup into parts for debugging purposes
def startup():
    print('Hello there. Welcome to your love- filled text based adventure. Im Candace your matchmaker.')
    player = {}
    player['name'] = input('Your name is...?')
    print('Nice to meet you', player['name'])
    c= ''
    while 'y' not in c and 'n' not in c:
        c = input('Are you ready to meet the love of your life? y/n')
        if 'n' in c.lower():
            print('Oh sorry to hear about that. Maybe next time')
            time.sleep(2)
            ##kills thread if they dont want to play
            quit()
        elif 'y' in c.lower():
            print('Perfect. Let us begin.')
            print('First tell me a little about yourself')
            player['gender'] = input('What is your gender?').lower()
            player['so'] = ""
            while ('male' not in player['so'] and 'lady' not in player['so'] and 'anyone' not in player['so']):
                if ('male' not in player['so'] and 'lady' not in player['so'] and 'anyone' not in player['so']):
                    player['so'] = input('Who are you looking to meet (male/lady/anyone)?')
                else:
                   mis()
            print('Perfect I think I know a few people you may like')
            return player
        else:
            mis()
##creates dictionaries for the three characters 
def loveForMoney():
    money = {}
    if ('male' in player['so']):
        money['name'] = 'Connor'
        money['gender'] = 'man'
    else:
        money['name'] = 'Kara'
        money['gender'] = 'lady'
    money['homeTown'] = 'Upper East Side'
    money['education'] = 'Brown, you know the Ivy'
    money['siblings'] = 'nanny and butler'
    money['herNick'] = 'love'
    money['adj'] = 'enjoy'
    money['hobby'] = 'sailing the harbors and tasting wine'
    money['n'] = 1
    money['h'] = 'a tall'
    money['food'] = 'cavier'
    return money

def loveForPity():
    pity = {}
    if ('lady' in player['so']):
        pity['name'] = 'Anna'
        pity['gender'] = 'lady'
    else:
        pity['name'] = 'Matt'
        pity['gender']= 'man'
    pity['homeTown'] = 'Staten Island'
    pity['education'] = 'high schooL'
    pity['siblings'] = '8 sibs'
    pity['adj'] = 'usually'
    pity['hobby'] = 'skateboard and do graffiti'
    pity['herNick'] = 'Bro'
    pity['n'] = 2
    pity['h'] = 'a lanky'
    pity['food'] = 'pb and j sandwiches'
    return pity

def loveLikely():
    likely = {}
    if ('male' in player['so']):
        likely['name'] = 'Harry'
        likely['gender'] = 'man'
    else:
        likely['name'] = 'Zohra'
        likely['gender'] = 'lady'
    likely['homeTown'] = 'Forest Hills'
    likely['education'] = 'Binghamton University'
    likely['siblings'] = 'my brother and sister'
    likely['hobby'] = 'take pictures and explore'
    likely['herNick'] = ''
    likely['adj'] = 'like to'
    likely['n'] = 3
    likely['h'] = 'an average- sized'
    likely['food'] = 'Thai food'
    return likely

##formats all the information into a paragraph
def characterIntros(d):
    print('Okay, this is Option',d['n'],':')
    print('**', d['h'], d['gender'],'walks in**' )
    print('Hey there', d['herNick'],'. My name is', d['name'],
          '. Im grew up in', d['homeTown'], 'with my', d['siblings'],'. I graduated from ', 
          d['education'],'.  I', d['adj'], d['hobby'], 'in my free time.')
    print('**',d['gender'],'exits **')

def loveSelection(d):
    print('Okay... with the Coronavirus going around many people arent available right now... but I found these three goodies all perfect for you! Ah Im so excited!')
    print('\n')
    characterIntros(loveForMoney())
    time.sleep(2)
    print('\n')
    characterIntros(loveForPity())
    time.sleep(2)
    print('\n')
    characterIntros(loveLikely())
    print('\n Hey', d['name'],'whatdya think?')
    c= ''
    while 'y' not in c and 'n' not in c:
        c = input('Anyone particularly cute? (y/n)')
        if 'n' in c:
            print('Sorry about that. Try again after this whole pandemic is all over.')
            time.sleep(2)
            quit()
        elif 'y' in c:
            xx = input('Well which option number????')
            if xx == 1:
                loveInterest= loveForMoney()
                return loveInterest
            elif xx==2:
                loveInterest= loveForPity()
                return loveInterest
            else:
                loveInterest = loveLikely()
                return loveInterest
        else:
            mis()
import time
player= startup()
lovey= loveSelection(player)
print('eeeee eeeee yay! I knew you two would click!',
      'Ill set up a date right now. \n **Candace leaves room momentarily**',
      '\n **she re-enters** \n ',lovey['name'], 'is free tonight. If you score well',
      'on the date, odds of love are in your favor, hun. Good luck. \n **she leaves before you',
      'can ask any questions** \n **you get dressed for your date**')
time.sleep(4)
print('**two hours and a hot shower later, you hear your doorbell ring** \n **Its', lovey['name'],'** \n',
      lovey['name'], ': I brought ', lovey['food'],'. Lets eat and get to know each other.')
score=[0,0,0,0,0,0,0,0,0,0]
print('Okay, we have ten lines to talk and Ill be keeping score of what you say to see if we click well.')
x=0
response= input('Well how are you today?')
iQ= ""
while x in range(10):
    if 'thank' in response or 'please' in response:
        score[x]= +1
        iQ= 'Wow manners, impressed. Anyways, tell me more about yourself'
    elif 'quit' in response:
        print('This was intended for me debugging, but Im glad you found the exit key. No love for you. Bye')
        time.sleep(2)
        quit()
    elif 'good' in response:
        iQ ='Good \n **they smile** \n So whats your favorite thing to do'
    elif 'bad' in response:
        iQ= 'Negative I see. Anything you find good in the world?'
        score[x] = -1
    elif 'sport' in response:
        score[x] =  +3
        iQ = 'I love sports! I used to play hockey as a kid. Tell me more'
    elif 'hockey' in response:
        score[x] =  +1
        iQ= 'Yay Im so glad you like hockey too! Anyways, whats your favorite food?'
    elif lovey['food'] in response and 'favorite' in response:
        score[x] =  -1
        iQ= 'Youre kissing ass. I just bought this because theres a restaurant right near my house. Id rather Ramen.'
    elif 'ramen' in response:
        score[x] = +1
        iQ = 'Love love love Ramen! Cheap and easy! But ugh.. I dont just like cheap and easy things I swear. Umm, coffee or tea?'
    elif 'love you' in response:
        score[x] = 1
        iQ = 'Aw cute. I could love you too'
    elif 'coffee' in response:
        score[x] =  + 1 
        iQ= 'Coffee is the best! Good choice haha, maybe we should get coffee sometime'
    elif 'hot choc' in response:
        score[x] =  +1
        iQ = 'Nhom nhom chocolate. With whipped cream so good'
    elif 'tea' in response:
        score[x] = -1
        iQ= 'Tea is gross and boring. I hope youre different, miss Matcha Iced Latte'
    elif 'like' in response:
        score[x] = 2
        iQ= 'I could like you too. What else do you like?'
    elif ' ex' in response:
        iQ= 'Why would you think its a good idea to tell me about your ex? Tell me about your favorite hot beverage instead'
        score[x] =  -2
    elif 'sorry' in response:
        score[x] = 1
        iQ= 'fine I accept your apology. Just keep talking.'
    elif 'yes' in response:
        score[x] =1
        iQ= 'Yay. GLad you think so'
    elif 'no' in response:
        score[x] = -1
        iQ = 'No? Oh okay. Try being nicer.'
    else:
        import random
        iQs= ['Interesting, tell me more', 'Nervous? Just talk','Anything else to share', 'Do you think this is going well? Say sorry', 'Ask me about sports', 'Talk to me!']
        i = random.randint(0,len(iQs)-1)
        iQ= iQs[i]
    response = input(iQ).lower()
    x= x+1
print('It was nice meeting you your response scores were', score)
import pandas as pd
s= pd.Series(score)
data = s.describe()
print(data)
if s.sum() > 5:
    print(lovey['name'], ': I like you.',player['name'],'Im glad we can be together \n **they lean in for a kiss mwuah! **', 
          '\n **happily ever after**')
else:
    print(lovey['name'],'Sorry... um youre sweet and all but I have to go... maybe Ill call you. Peace! \n **they sprint out the door** \n  Try to score higher next time. \n \n GAME OVER')
    
    




