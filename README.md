# LPML-bot
A discord bot that can make roll calls and print homework. It was originally developed for the SAS server, but now everything is complicated (chil).

# INSTALL
git clone https://github.com/CoderBogdasha/LPML-bot/

cd LPML-bot/

pip install requests

python bot.py

# iNSTUCTION
use command:

* /homework - to print all homeworks

* /print_homework homework_number - to print list of exercises in the given homework

* /print_exercise homework_number exercise_number - to print exercise

* /create_homework - to create homework (you must have a special role to run this command (see the section SETTINGS in config.py))

* /edit_homework homework_number exercise_number image_scr - to edit exercise image link (you must have a special role to run this command (see the section SETTINGS in config.py))

(If you entered a different command prefix, the commands will be different for you)

# SETTINGS in config.py
TOKEN - this is a discord token of your bot

way - this is the path to your .dat file (use \\\\ instead of \\)

students - this is a list that contains the last name and first name of all students

color - this is the color of the left lane of the message in the discord

bot_activity - this is the text that will be displayed as a status (Playing #####)

edit_role - this is a role that can create and edit homework

prefix - this is discord command prefix
