import re

re_cmd = re.compile('\$ (?P<cd>cd (?P<dir>(\w+)|(\.\.)))|(?P<ls>ls)')
re_file = re.compile('(?P<mem>\d+) (?P<filename>[\w\.]+)')
re_dir = re.compile('dir (?P<dirname>\w+)')

fd = open('Day7.txt', 'r')

home_dir = {}
cur_dir = home_dir
cur_pos = []
CMD = None
for line in fd:
    if re_cmd.search(line):
        res = re_cmd.match(line)
        if res['ls']:
            # CMD = 'ls'
            continue
        elif res['dir'] == '/':
            cur_pos = [home_dir]
            cur_dir = home_dir
        elif res['dir'] == '..':
            cur_dir = cur_pos.pop()
        else:
            cur_dir[res['dir']] = {'files':[]}
            cur_pos.append(cur_dir[res['dir']])
            cur_dir = cur_dir[res['dir']]
    elif re_file.search(line):
        res = re_file.match(line)
        fileinfo = (res['filename'], res['mem'])
        if 'files' not in cur_dir.keys():
            cur_dir['files'].append(fileinfo)
    elif re_dir.search(line):
        res = re_dir.match(line)
        if res['dir'] not in cur_dir.keys():
            cur_dir[res['dir']] = {}


def calc_sum(file_list):
    return sum(*[info[1] for info in file_list])


visited_dirs = {'/': 0}
cur_pos = ['/']
cur_dir = home_dir
to_visit = [*list(home_dir.keys()).remove('files')]
while to_visit:
    cur_dir = to_visit.pop(to_visit.index(cur_pos[-1]))
