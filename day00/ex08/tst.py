import sys,time,random, os
def progressBar(count_value, total, suffix=''):
	bar_length = os.get_terminal_size().columns - 25
	filled_up_Length = int(round(bar_length* count_value / float(total)))
	percentage = round(100.0 * count_value/float(total),1)
	bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
	sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
	sys.stdout.flush()
for i in range(11):
	time.sleep(random.random())
	progressBar(i,10)
#This code is Contributed by PL VISHNUPPRIYAN
