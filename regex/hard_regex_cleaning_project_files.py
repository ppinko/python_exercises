"""
https://edabit.com/challenge/NC888jKPkquSDqaaH
"""


import re


def clean_up(files, sort):
    all_names = ':'.join(files)
    ans, s = [], []
    if sort == 'prefix':
        for i in re.findall(r'\w+(?=\.)', all_names):
            if i not in s:
                s.append(i)
        for i in s:
            ans.append(re.findall('{0}[^\:]+'.format(i), all_names))
    else:
        for i in re.findall(r'(?<=\.)\w+', all_names):
            if i not in s:
                s.append(i)
        for i in s:
            ans.append(re.findall('\w+\.{0}'.format(i), all_names))
    return ans


assert clean_up(['music_app.js', 'music_app.png', 'music_app.wav', 'tetris.png', 'tetris.js'], 'prefix') == \
       [['music_app.js', 'music_app.png', 'music_app.wav'], ['tetris.png', 'tetris.js']]
assert clean_up(['_1.rb', '_2.rb', '_3.rb', '_4.rb'], 'suffix') == [['_1.rb', '_2.rb', '_3.rb', '_4.rb']]
assert clean_up(['_1.rb', '_2.rb', '_3.rb', '_4.rb'], 'prefix') == [['_1.rb'], ['_2.rb'], ['_3.rb'], ['_4.rb']]
assert clean_up(['project1.html', 'project2.html', 'project1.css', 'project2.css', 'project1.js', 'project2.js'], 'suffix') == \
       [['project1.html', 'project2.html'], ['project1.css', 'project2.css'], ['project1.js', 'project2.js']]

print('Success')