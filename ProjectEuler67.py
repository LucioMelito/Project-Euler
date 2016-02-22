import time

rows = []
with open('/Users/luciomelito/Documents/Python/Project Euler/Problem67Data') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
        
# define a recursive function to create partial sums by row
def recSumAtRow(rowData, rowNum):
    # iterate over the given row
    for i in range(len(rowData[rowNum])):
        # add the largest of the values below-left or below-right
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    # base case
    if len(rowData[rowNum])==1: return rowData[rowNum][0]
    # recursive case
    else: return recSumAtRow(rowData, rowNum-1)

start = time.time()    
result = recSumAtRow(rows, len(rows)-2)
elapsed = time.time() - start

print 'The maximum sum is ' + str(result) + ' and was found in ' + str(elapsed) + ' s'