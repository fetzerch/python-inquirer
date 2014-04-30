import os
import sys
import re
sys.path.append(os.path.realpath('.'))
from pprint import pprint

import inquirer

questions = [
    inquirer.Text('name',
                  message="What's your name"),
    inquirer.Text('surname',
                  message="What's your surname"),
    inquirer.Text('phone',
                  message="What's your phone number",
                  validation=lambda x: re.match('\d+', x),
                  )
]

answers = inquirer.prompt(questions)

pprint(answers)
