import pygame as pg
import random

window = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()

cell_rects = []
cells_filled = {}

filled_cell_amount = 0
empty_cell_amount = 0

def draw_grid():
    for x in range(0, window.get_width(), 10):
        pg.draw.line(window, (255, 255, 255), (x, 0), (x, window.get_height()))
    
    for y in range(0, window.get_height(), 10):
        pg.draw.line(window, (255, 255, 255), (0 ,y), (window.get_width(), y))

def find_cells():
    for x in range(0, window.get_width(), 10):
        for y in range(0, window.get_height(), 10):
            cell = pg.Rect(x, y, 10, 10)
            cell_rects.append(cell)
            
def fill_random_cells():
    global filled_cell_amount, empty_cell_amount
    
    for cell in cell_rects:
        if random.choice([True, False]):
            cells_filled[cell.topleft] = True
            filled_cell_amount += 1
        else:
            cells_filled[cell.topleft] = False
            empty_cell_amount += 1
            
def draw_filled_cells():
    for index, cell_location in enumerate(cells_filled):
        if cells_filled[cell_location]:
            pg.draw.rect(window, (0, 255, 0), cell_rects[index])
            
def check_nearby_tiles():
    for index, location in enumerate(cells_filled):
        left_index = index-1
        left_location = cell_rects[left_index].topleft
        left_filled = cells_filled[left_location]
        
        right_index = index+1
        try:
            right_location = cell_rects[right_index].topleft
        except:
            continue
        right_filled = cells_filled[right_location]
        
        filled = cells_filled[location]
        
        if left_filled and right_filled and not filled:
            cells_filled[location] = True

running = True

while running:
    window.fill((0, 0, 255))
    
    draw_grid()
    draw_filled_cells()
    
    clock.tick(60)
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RETURN:
                cells_filled = {}
                cell_rects = []
                filled_cell_amount = 0
                empty_cell_amount = 0
                
                find_cells()
                fill_random_cells()
            elif event.key == pg.K_SPACE:
                print("rawr")
                check_nearby_tiles()