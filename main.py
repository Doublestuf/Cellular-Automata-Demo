import pygame as pg
import random

pg.font.init()

window = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()

cell_rects = []
cells_filled = {}

width_cell_rects = []

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
            
def find_cells_width():
    for y in range(0, window.get_width(), 10):
        for x in range(0, window.get_height(), 10):
            cell = pg.Rect(x, y, 10, 10)
            width_cell_rects.append(cell)
            
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

        if left_filled and right_filled:
            cells_filled[location] = True
        elif not left_filled and not right_filled:
            cells_filled[location] = False
            
def check_nearby_tiles_width():
    for index, location in enumerate(cells_filled):
        left_index = index-1
        left_location = width_cell_rects[left_index].topleft
        left_filled = cells_filled[left_location]
        
        right_index = index+1
        try:
            right_location = width_cell_rects[right_index].topleft
        except:
            continue
        right_filled = cells_filled[right_location]
        
        if left_filled and right_filled:
            cells_filled[location] = True
        if not left_filled and not right_filled:
            cells_filled[location] = False

running = True
iterations = False

find_cells_width()

while running:
    window.fill((0, 0, 255))
    
    draw_grid()
    draw_filled_cells()
    
    if iterations == -1:
        font = pg.font.Font(pg.font.get_default_font(), 50)
        text = font.render("Cleaning up...", False, (255, 255, 255))
        window.blit(text, (0, 0))
        
        check_nearby_tiles_width()
        check_nearby_tiles_width()
        check_nearby_tiles_width()
        check_nearby_tiles()
        check_nearby_tiles()
        check_nearby_tiles()
        
        iterations = False

    if iterations:
        check_nearby_tiles_width()
        check_nearby_tiles()
        draw_filled_cells()
        
        font = pg.font.Font(pg.font.get_default_font(), 50)
        text = font.render(f"Iterations Left: {iterations}", False, (255, 255, 255))
        window.blit(text, (0, 0))
        
        iterations = iterations - 1 if iterations > 1 else -1
    
    clock.tick()
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
                iterations += 10
            elif event.key == pg.K_b:
                check_nearby_tiles()
            elif event.key == pg.K_n:
                check_nearby_tiles_width()
            elif event.key == pg.K_m:
                check_nearby_tiles_width()
                check_nearby_tiles()