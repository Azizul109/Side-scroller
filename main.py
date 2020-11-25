
if __name__ == "__main__": # it will only load so that i can understand that my file is running
    print('Loading main')
    
    import pygame # it will import pygame
    import menu # it will import menu(from where all file will be generate)
    
    gameExit = False
    menuScreen = menu.AddScreen()
    menuScreen.run()
    pygame.display.quit()
    pygame.quit()

    
