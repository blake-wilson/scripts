import sys
import fileinput

# first argument to script: the number of columns in the produced table
# example: python table_maker.py 10 < emoji_data.txt > emoji_table

num_cols = int(sys.argv[1]) if len(sys.argv) > 0 else sys.maxint

col_ctr = 0
print('<tr>')
for line in fileinput.input(sys.argv[2:]):
    filtered = line.split('#')[0].strip()
    if len(filtered) == 0:
	continue
    before_semi = filtered.split(';')[0].strip()
    start = before_semi.split('..')[0]
    after = before_semi.split('..')[1] if len(before_semi.split('..')) > 1 else start

    for i in range(int(start, 16), int(after, 16)):
	if col_ctr >= num_cols:
            print('</tr><tr>')
	    col_ctr = 0
	print('<td>' + '&#' + str(i) + ';' + '</td>')
	col_ctr += 1

print ('</tr>')
