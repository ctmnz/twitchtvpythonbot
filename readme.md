Python simple twtich.tv irc bot

How to run it?


1. Register username on twitch.tv
2. Follow instructions here http://help.twitch.tv/customer/portal/articles/1302780-twitch-irc in order to obtain oauth token
3. Download this bot on computer with installed python. git clone https://github.com/ctmnz/twitchtvpythonbot.git 
4. Edit bot.cfg 
 - twitch_user=yourtwitchusername (put your twitch username obtained from step 1)
 - bot_connect_password=oauth:this-is-your-oauth-token (put your twitch oauth token obtained from step 2)
 - bot_autojoin_channels=#channeltojoin,#channeltojoin2 (put desired irc channel(s) to join)
5. run the bot with command: python bot.py
6. Enjoy 
7. Write an email with suggestions for further development to daniel.stoinov@gmail.com
 
