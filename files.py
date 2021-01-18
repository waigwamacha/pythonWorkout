from io import StringIO
from collections import Counter


fakefile = StringIO('''
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
''')

def get_final_line(filename):
    final_line = ''
    vowels = 'aeiou'
    for current_line in filename:
        final_line = current_line
    # for x in vowels:
    #     for char in filename:
    #         if char == x:
    #             count = sum[x]
    #         print(count)
            
    print(final_line)


get_final_line(fakefile)