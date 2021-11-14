import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
random.seed = 1998
ON = 255
OFF = 0
vals = [ON, OFF]

def populate(rows:int, cols:int)->np.array:
  return np.random.choice(vals, rows*cols, p=[0.2, 0.8]).reshape(rows, cols)

def display(grid:np.array, rows:int, cols:int)->str:
  string = ''
  for i in range(rows):
    for j in range(cols):
      if(grid[i][j]==1):
        string+='x '
      else: string+='  '
    string+='\n'
  return string


def update(frameNum, img, grid:np.array, rows:int, cols:int) -> np.array:
  grid_new = grid.copy()
  
  for i in range(rows):
    for j in range(cols):
      living_neighbors = 0
      dead_neighbors = 0
      #count neighbors
      total = int((grid[i, (j-1)%cols] + grid[i, (j+1)%cols] +
                         grid[(i-1)%rows, j] + grid[(i+1)%rows, j] +
                         grid[(i-1)%rows, (j-1)%cols] + grid[(i-1)%rows, (j+1)%cols] +
                         grid[(i+1)%rows, (j-1)%cols] + grid[(i+1)%rows, (j+1)%cols])/255)
      if grid[i][j]==ON:
        if total < 2 or total>3:
          grid_new[i][j] = OFF
        else: grid_new[i][j] = ON
      else:
        if total == 3:
          grid_new[i][j] = ON

    # update data
  img.set_data(grid_new)
  grid[:] = grid_new[:]
  return img,
      
      
      
      







  
if __name__ == '__main__':
  rows = 60
  cols = 40
  grid = populate(rows,cols)
  
  fig, ax = plt.subplots()
  img = ax.imshow(grid, interpolation='nearest')
  ani = animation.FuncAnimation(fig, update, fargs=(img, grid, rows, cols, ),
                                  frames = 10,
                                  interval=50,
                                  save_count=50)

  plt.show()





