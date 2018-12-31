import re


def main():
    new_talk = False
    current_talk= ''
    the_date = 'day 3'
    the_time = ''
    the_place = ''

    for line in open('day3.txt'):

        # This marks the start of a talk in the plan
        if line.startswith('#'):
            #print(line.strip())
            new_talk = True
            continue

        if new_talk and line.startswith('['):
            _, the_time, _, the_place = line.strip().split()
            continue

        if new_talk and line.startswith('[') is False:
            #print(line.strip())
            current_talk = line.strip()
            new_talk = False
            continue

        # The talk has a marker for a french translation
        if current_talk and re.match(r'^\s*→\s*fr\s*:', line):
            # there is more than one translator
            print('La présentation "{}" ({} {} à {}) sera traduite en Francais'.format(current_talk, the_date, the_time, the_place))
            continue

        # An empty line is the end of a talk block
        if not line.strip():
            current_talk = ''
            the_time = ''
            the_place = ''
            continue
