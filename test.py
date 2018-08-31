# types of commands
# 1) commands with no arguments, static output
# 		!xd, !brna
# 2) commands with 1+ argument, dynamic output
#		!ban ____
# 3) commands where user is argument
# 		!points
# 4) admin commands (with or without arguments)
asdf = "asjdfkl;a"
test_str = r":hwangbroxd!hwangbroxd@hwangbroxd.tmi.twitch.tv PRIVMSG #hwangbroxd :!lfjdk"
from pyparsing import Word, alphas, alphanums, restOfLine, Suppress, Optional
def parsetest():
	command = "!" + Word(alphas).setResultsName("command") + restOfLine.setResultsName("arg")
	message = "#" + Word(alphanums + "_").setResultsName("username") + ":!" + Word(alphas).setResultsName("cmd") + restOfLine.setResultsName("msg")
	# for t,s,e in command.scanString(test_str):
	# 	print("command:",t.command, "\nextra:", str.lstrip(t.arg))
	x = list(message.scanString(test_str))
	if x:
		print(x[0][0].username, x[0][0].cmd, 'msg:', x[0][0].msg)
	ff = message.scanString(test_str)
	if list(ff):
		print("alive")
	# for t,s,e in message.scanString(test_str):
	# 	print(t.username, ":", t.msg)

#parsetest()

import api
import cfg
import requests, cfg
url = 'https://api.twitch.tv/helix/streams?user_login=hwangbroxd'
print(url)
r2 = requests.get(url=url, headers=cfg.HEADERS)
print(r2.json())
#url = '''https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials&scope=user:edit:broadcast user:edit'''.format(cfg.CLIENT_ID, cfg.secret)
#url = r'https://id.twitch.tv/oath2/token?client_id={}&client_secret={}&grant_type=client_credentials&scope=user:read:broadcast'.format(cfg.CLIENT_ID, cfg.secret)
#r = requests.get(r'http://id.twitch.tv/oath2/validate', headers={'Authorization': 'OAuth ' + cfg.TOKEN})
# data = {'channel': {'game': 'League of Legends'}}
# r = requests.put(cfg.URL, headers=cfg.HEADERS, json=data)
# print(r.json())