import irclib
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('bot.cfg')

irc_server = config.get('irc_server_settings','irc_server')
irc_port = config.get('irc_server_settings','irc_port')
bot_connect_password = config.get('bot_settings','bot_connect_password')
bot_nick = config.get('bot_settings','twitch_user')
bot_ident = config.get('bot_settings','twitch_user')
bot_real_name = config.get('bot_settings','twitch_user')
bot_owner = config.get('bot_settings','twitch_user')
bot_autojoin_channels = config.get('bot_settings','bot_autojoin_channels')

myirc = irclib.irc(irc_server,irc_port,bot_nick,bot_ident,bot_real_name,bot_autojoin_channels,bot_connect_password)
myirc.connect()

