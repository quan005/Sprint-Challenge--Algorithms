#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n**2) : Because within the while loop "a" grows n * n times plus a itself which is constant


b) O(nlogn) : Because i is O(n), and j is doubled each time in the while loop, which gives it a O(logN) run time to reach target. Making it O(n)*O(logn).


c) O(n) : Because its only ran n times (or to the base case)

## Exercise II

- building has n floors
- egg breaks on floor f and higher
- ground equal 0


  # First we divide the floors in half
  currentFloor = floors/2
  highFloors = len(floors)-1
  lowFloors = floors[0]
  
  # Drop an egg
  dropped += 1

  # If broken equals true, then we remove the highFloors above currentFloor
  highFloors = currentFloor

  -- Divide the remainder floors in half and drop an egg
  currentFloor = currentfloor/2
  dropped += 1

  -- Repeat until broken equals true then return currentFloor

  # If broken equals false, we remove all the floors below
  lowFloors = currentFloors

  -- Divide the remainig floors in half and drop an egg
  currentFloor = highfloors - (currentFloor/2)
  dropped +=1

  -- Repeat until broken equals true then return currentFloor

Time complexity will be O(logn)