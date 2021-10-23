import pygame

def main():
    pygame.init()
    team = {"lead": "?", "backend": "?", "frontend": "?"}
    print("Software Lead is:", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:" , team["frontend"])
main()
