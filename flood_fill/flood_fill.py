matrix =[[2,3,3,3,3,3,4,4,4,4,4,4],
	[2,3,3,3,3,3,4,4,4,4,4,4],
	[3,3,3,1,3,3,4,1,4,4,0,4],
	[3,3,1,1,1,3,1,1,1,4,4,4],
	[3,1,1,1,1,1,1,1,1,1,4,4],
	[3,1,1,0,0,0,0,0,1,1,4,4],
	[3,1,1,0,0,0,0,0,1,1,4,4],
	[2,1,1,1,1,0,0,0,1,1,2,2],
	[2,1,1,1,0,0,0,0,1,2,2,2],
	[2,2,1,1,1,0,0,2,2,2,1,0],
	[2,2,2,1,1,0,0,2,2,2,1,1],
	[2,2,2,2,2,2,2,2,2,0,1,0]
	]

def flood_fill(x ,y, old, new):
    print(x, y)
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix):
        return
    # secondly, check if the current position equals the old value
    if matrix[y][x] != old:
        return
    # thirdly, set the current position to the new value
    matrix[y][x] = new
    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)

flood_fill(0,0,2,1)
print(matrix)