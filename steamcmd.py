import subprocess
import config, color
def run(args):
	command = args.split()
	command.insert(0, "./steamcmd.sh")
	print "Running command"
	print command
	subprocess.call(command, cwd=config.STEAM_PATH)
