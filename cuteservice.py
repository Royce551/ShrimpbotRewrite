import discord
import random
from discord.ext import commands
#CuteService Ver. 1, Patch 0.
def cuver():
    return 'Version 1 Patch 2'
def cute(flag ='all'):
    one = 0
    two = 0
    if flag == 'all':
        one = 1
        two = 17
    elif flag == 'anime':
        one = 1
        two = 16
    elif flag == 'doggos':
        one = 17
        two = 17
    else:
        one = 1
        two = 17
    cutenumber = str(random.randint(one,two))
    cutesend = 'p'
    if cutenumber == '1':
        cutesend = 'cute1.png'
    elif cutenumber == '2':
        cutesend = 'cute2.png'
    elif cutenumber == '3':
        cutesend = 'cute3.png'
    elif cutenumber == '4':
        cutesend = 'cute4.png'
    elif cutenumber == '5':
        cutesend = 'cute5.png'
    elif cutenumber == '6':
        cutesend = 'cute6.png'
    elif cutenumber == '7':
        cutesend = 'cute7.png'
    elif cutenumber == '8':
        cutesend = 'cute8.png'
    elif cutenumber == '9':
        cutesend = 'cute9.png'
    elif cutenumber == '10':
        cutesend = 'cute10.png'
    elif cutenumber == '11':
        cutesend = 'cute11.png'
    elif cutenumber == '12':
        cutesend = 'cute12.jpg'
    elif cutenumber == '13':
        cutesend = 'cute13.png'
    elif cutenumber == '14':
        cutesend = 'cute14.png'
    elif cutenumber == '15':
        cutesend = 'cute15.png'
    elif cutenumber == '16':
        cutesend = 'cute16.jpg'
    elif cutenumber == '17':
        cutesend = 'placeholder.png'
    return cutesend

def hug():
    hugsend = 'p'
    huginfo = 'p'
    hugnumber = str(random.randint(1,1))
    if hugnumber == '1':
        hugsend = 'hug1.png'
        huginfo = '''
         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
By うさみん | https://twitter.com/usamin1211/status/1079953811702042624'''
        return hugsend, huginfo;

def slap():
    slapsend = 'p'
    slapinfo = 'p'
    slapnumber = str(random.randint(1,1))
    if slapnumber == '1':
        slapsend = 'slapimage.gif'
        slapinfo = '''
         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sources not available, sorry \:('''
        return slapsend, slapinfo;

def pet():
    petsend = 'p'
    petinfo = 'p'
    petnumber = str(random.randint(1,1))
    if petnumber == '1':
        petsend = 'petimage.png'
        petinfo = '''
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sources not available, sorry \:('''
        return petsend, petinfo;

def help(page):
    helpsend = 'p'
    if page == 'changelog':
        helpsend = '''**changelog**
        s:changelog (page number)
        Lists all the most recent changes to Shrimpbot.
        Page 1 - Shrimpbot 16x
        Page 2 - Shrimpbot 15x
        Page 3 - Shrimpbot 14 and 13.'''
        return helpsend
    elif page == 'cute':
        helpsend = '''**cute**
        s:cute (category)
        Gives you a random cute picture (usually anime).

        __**Category**__ - can be...
        **all** - All available pictures
        **anime** - Anime only
        **doggos** - Dogs.
        (Defaults to "all")'''
        return helpsend
    elif page == 'useDM':
        helpsend = '''**useDM**
        s:useDM
        Opens a direct message with the user.
        Note - You can also simply right click the bot and select "Message".
        # This command does not need to be typed in all the way!'''
        return helpsend
    elif page == 'information':
        helpsend = '''**information**
        Gives you information about the bot, including version number of the bot itself and the cute service, and
        a link to a page about the license the bot uses, and credits for people who helped with the bot.'''
        return helpsend
   #elif page == 'cool':
       #helpsend = '''**cool**
        #Says that you are cool.'''
       #return helpsend
    elif page == 'messages':
        helpsend = '''**messages**
        Gives you a count of all messages you sent in the channel you executed the command in since the bot started running, up to an arbitrairy limit of 100.
        # This command does not need to be typed in all the way!'''
        return helpsend

def get8ball():
    ball = random.randint(1,20)
    result = ''
    positive = ''
    if ball == 1:
        result = 'It is certain.'
    elif ball == 2:
        result = 'It is decidedly so.'
    elif ball == 3:
        result = 'Without a doubt.'
    elif ball == 4:
        result = 'Yes - definitely.'
    elif ball == 5:
        result = 'You may rely on it.'
    elif ball == 6:
        result = 'As I see it, yes.'
    elif ball == 7:
        result = 'Most likely.'
    elif ball == 8:
        result = 'Outlook good.'
    elif ball == 9:
        result = 'Yes.'
    elif ball == 10:
        result = 'Signs point to yes.'
    elif ball == 11:
        result = 'Reply hazy, try again.'
    elif ball == 12:
        result = 'Ask again later.'
    elif ball == 13:
        result = 'Better not tell you now.'
    elif ball == 14:
        result = 'Cannot predict now.'
    elif ball == 15:
        result = 'Concentrate and ask again.'
    elif ball == 16:
        result = 'Don\'t count on it.'
    elif ball == 17:
        result = 'My reply is no.'
    elif ball == 18:
        result = 'My sources say no.'
    elif ball == 19:
        result = 'Outlook not so good.'
    elif ball == 20:
        result = 'Very doubtful.'
    if ball < 10:
        positive = 'P'
    elif ball < 15:
        positive = 'C'
    else:
        positive = 'N'
    return result, positive;
        
        
        

