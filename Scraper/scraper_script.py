import os
import sys
week = sys.argv[1]
sections = [
    'cse-a-week-',
    'cse-b-week-',
    'cse-c-week-',
    'cse-d-week-',
    'cse-e-week-',
    'cse-f-week-',
    'cse-g-week-',
    'cse-h-week-',
    'cse-i-week-',
    'cse-j-week-',
    'cse-k-week-',
    'cse-l-week-',
    'aiml-a-week-',
    'aiml-b-week-',
    'aiml-c-week-'
]

for i in sections:
    while(os.path.exists(os.path.join(os.getcwd(),i+week+'.csv'))==False):
        # print(i+week)
        os.system(f"./start.sh {i+week}")

# x ='cse-b-week-2'
# os.system(f"./start.sh '{x}'")
