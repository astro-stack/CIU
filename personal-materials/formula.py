x = int(input('Number of companies interviewed: '))
y = int(input('Number of offers received: '))
import math
value = 100 * math.log(x) * y / x
print('Value:', value)
# save result in a file and the date
import datetime
now = datetime.datetime.now()
with open('result-{}.txt'.format(now.strftime('%Y-%m-%d-%H-%M-%S')), 'w') as f:
    f.write(str(value) + '\n')
    f.write(now.strftime('%Y-%m-%d %H:%M:%S') + '\n')