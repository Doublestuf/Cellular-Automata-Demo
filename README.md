# Cellular-Automata-Demo
A demo of the cellular automata system as used for world generation

a slightly imperfect implementation, made in pygame

How it works:
    Randomly makes each tile either grass or water
    Checks if the tiles to the left and right of a tile are grass. If the middle tile is water, it changes to grass
    Checks if the tiles to the left and right of a tile are water. If the middle tile is grass, it changes to water
    Repeat 10x
    That's it

Controls:
    ENTER to randomly fill the tiles
    SPACE to iterate over the tiles 10 time
    B to iterate over the tiles vertically
    N to iterate over the tiles horizontally
    M to iterate over the tiles horizontally, then vertically

Hope this helps i guess
Feel free to use in any project, educational, non-commercial, commercial, credit optional