import curses

def main(screen,mg):

# this variable is the top cordinate by top i mean y

    map = ["┌─────────┬─────────────────────────────┐",                                                                                                                   
           "│         │                             │",                                                                  
           "│         │                             │",                                                                                                                   
           "│         │                             │",                                                                                                                   
           "│         │                             │",                                                                                                                   
           "│         └─────────│                   │",                                                                                                                                                                                                                                                                                                                     
           "│                   │                   │",                                                                                                                   
           "│                   │                   │",                                                                                                                   
           "│                   │                   │",                                                                                                                   
           "│                   │                   │",                                                                                                                   
           "│                   │                   │",                                                                                                                   
           "│                   │                   │",                                                                                                                   
           "│                   │                   │",                                                                                                                   
           "│                   │                   │",                                                                                                                   
           "│                   │                   │",                                                                                                                                                                                                                                  
           "│                   │                   │",                                                                                                                   
           "│                   │───────────────────│",
           "│                                       │",
           "│                                      T│",
           "│                                       │",
           "└───────────────────────────────────────┘"]

    



# our player coordinates
#player y coordinate



    player_y = 1

#player x coordinate
    player_x = 1


    s_y = 1

    s_x = 1

    show_s = False

    show_T = True

    

    for y,row in enumerate(map):
        screen.addstr(y,0,row)

    screen.addstr(player_y,player_x,"p")
    screen.addstr(22, 0, f"x={player_x} y={player_y}")
    show_s = movement(screen,player_y,player_x,map,s_y,s_x,show_s,mg)
        ##screen.addstr(s_y,s_x,"S")
        #movement(screen,player_y,player_x,map)
        #addstring(screen,player_y,player_x,map)
        #screen.addstr(s_y,s_x,"S")
        #screen.refresh()

    #draw_map(screen,top,left,right,bottom,horizontal,vertical,zero_x,wall_boundary_x,wall_boundary_y,wall_boundary_x_range,player_x,player_y,wall_fill,left_corner)
    #hallway(screen,top,left,bottom,right,horizontal,vertical)
def movement(screen,player_y,player_x,map,s_y,s_x,show_s,mg):
    #if map[player_y][player_x] == " ":

        Target_reached = "0"


         

        move = True
        while move:
            

                key = screen.getch()
                player_down = curses.KEY_DOWN
        
                player_up = curses.KEY_UP
                #if y == wall_boundary_y and x in wall_boundary_x:
                #if y == 4 and key == player_down and x in wall_boundary_x:
                # y -= 1
                #player_down = curses.KEY_DOWN

                #player_up = curses.KEY_UP

                if key == player_up:

                    if map[player_y - 1][player_x] == " " :
            
                        player_y -= 1

                    elif map[player_y - 1][player_x] == "T" :

                        show_s = True

                    #return show_s

                        
                elif key == player_down:

                    if map[player_y + 1][player_x] == " ":

                        player_y += 1

                    elif map[player_y + 1][player_x] == "T":

                        show_s = True

                    #return show_s

                        

                elif key == curses.KEY_LEFT:

                    if map[player_y][player_x - 1] == " ":

                        player_x -= 1

                    elif map[player_y][player_x - 1] == "T":

                        show_s = True

                    #return show_s

                elif key == curses.KEY_RIGHT:

                    if map[player_y][player_x + 1] == " ":

                        player_x += 1

                    elif map[player_y][player_x + 1] == "T":

                        show_s = True

                    #return show_s
                
                addstring(screen,player_y,player_x,map,s_y,s_x,show_s,mg)

def addstring(screen,player_y,player_x,map,s_y,s_x,show_s,mg):

        for y,row in enumerate(map):
            screen.addstr(y,0,row)

        if show_s == True:
            screen.addstr(0,0,mg)
            #screen.addstr(s_y, s_x, "S")          

        screen.addstr(player_y,player_x,"p")
        screen.addstr(22, 0, f"x={player_x} y={player_y}")
                #draw_map(screen,top,left,right,bottom,horizontal,vertical,zero_x,wall_boundary_x,wall_boundary_y,wall_boundary_x_range,player_x,player_y,wall_fill,left_corner)
                #hallway(screen,top,left,bottom,right,horizontal,vertical)
        screen.refresh()
        #else:
             #pass
 
if __name__ == "__main__":
    curses.wrapper(main)