import os
from random import randint

try:
    for i in range(1, 2):
        try:
            for j in range(0, 2):
                date = str(365+i) + ' days ago'
                with open('changes.txt', 'a') as file:
                    file.write(date)
                os.system('git add .')
                os.system('git commit --date="' + date + '" -m "comment"')
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
