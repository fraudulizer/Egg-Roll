# Fraudulizer's Egg Roll

## Synopsis
In this game, you are given a grid of objects. Each object is represented by an emoji on the grid. Your task is to roll the eggs in the grid to a nest in the grid.  
Each nest in the grid can only fill 1 egg. Eggs will stop if they hit a filled nest or a brick. Eggs will break if they hit the pan.  

Brick = 🧱  
Egg = 🥚  
Green = 🟩  
Nest = 🪹  
Done = 🪺  
Pan = 🍳  

You are only given a set amount of moves to roll the eggs into the nests.

## Controls
Input **F** to roll the eggs upwards on the grid.  
Input **B** to roll the eggs downwards on the grid.  
Input **L** to roll the eggs leftwards on the grid.  
Input **R** to roll the eggs downwards on the grid.  

You **CAN** combine instructions into one string to do multiple operations in one command.  
Press **ENTER** after inputting your desired instructions to ensure that your instructions are read by the program.

## Scoring
You are given 10 points for each egg rolled into the nest, plus bonus points for each move left on that move.
You lose 5 points for each egg that gets destroyed by a pan.  

## Dependencies
Python 3.13  
os and time  