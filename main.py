import pygame
from src import controller


def main():
    pygame.init()
    team = {"lead": "Christopher Yu", "backend": "Young Seo (Esther) Hur", "frontend": "Ashley Yu"}
    print("Software Lead is:", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:" , team["frontend"])
    main_window = controller.Controller()
    main_window.mainloop()


main()
