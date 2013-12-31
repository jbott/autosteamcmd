import json, color

def load_file(file):
	f = open(file, 'r')
	return json.load(f)

def list_games(games):
	name_width = max(len(row['name']) for row in games )# Padding for name
	color.printcln("Name:".ljust(name_width) + '    ' + "App ID:".ljust(10) + '    ' + "Aliases:")
	for game in games:
		color.printcln(game['name'].ljust(name_width) + '    ' + str(game['app_id']).ljust(10) + '    ' + "".join(alias + ' ' for alias in game['aliases']))
