import re


def main():
    new_talk = False
    current_talk= ''
    the_date = '3'
    the_time = ''
    the_place = ''

    for line in open('/home/informancer/Downloads/36c3-day3-latest.txt'):

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
            print('La présentation "{}" (jour {} {} à {}) sera traduite en Francais.'.format(current_talk, the_date, the_time, the_place))
            continue

        # The talk has a marker for an english translation
        if current_talk and re.match(r'^\s*→\s*en\s*:', line):
            # there is more than one translator
            print('The talk "{}" (day {} {} in {}) will be translated in english.'.format(current_talk, the_date, the_time, the_place))
            continue

        # The talk has a marker for a german translation
        if current_talk and re.match(r'^\s*→\s*de\s*:', line):
            # there is more than one translator
            print('Der Vortrag "{}" (Tag {} {} im Raum {}) wird auf Deutsch übersetzt.'.format(current_talk, the_date, the_time, the_place))

        # The talk has a marker for a polish translation
        if current_talk and re.match(r'^\s*→\s*pl\s*:', line):
            # there is more than one translator
            print('Wykład "{}" (dzień {}, {} w sali {}) będzie tłumaczony na polski.'.format(current_talk, the_date, the_time, the_place))

        # The talk has a marker for a spanish translation
        if current_talk and re.match(r'^\s*→\s*es\s*:', line):
            # there is more than one translator
            print('La charla "{}" (día {}, a las {}, salón {}) será traducida al español.'.format(current_talk, the_date, the_time, the_place))

        # The talk has a marker for a spanish translation
        if current_talk and re.match(r'^\s*→\s*ru\s*:', line):
            # there is more than one translator
            print('Лекция «{}» (день {} {} в зале {}) будет переведена на английский'.format(current_talk, the_date, the_time, the_place))
        
        # An empty line is the end of a talk block
        if not line.strip():
            current_talk = ''
            the_time = ''
            the_place = ''
            continue
