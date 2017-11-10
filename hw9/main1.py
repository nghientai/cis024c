import sorthelper
import sys

getArgs = sys.argv
numbers = []
for i in range(1,len(getArgs)):
    numbers.append(int(getArgs[i]))


sorthelper.sortNumbers(numbers)
print numbers