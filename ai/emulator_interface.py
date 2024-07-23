from gym import Env
import numpy as np
import pygame  # Import Pygame für die Anzeige

class LakeSnesInterface(Env):
    def __init__(self, rom_path):
        # ... (Initialisierung des Emulators)
        self.screen = pygame.display.set_mode((256, 224))  # Fenster erstellen (Größe anpassen)
        pygame.display.set_caption("LakeSnes mit KI")

    # ... (reset und step Methoden)

    def render(self, mode='human'):
        if mode == 'human':
            # Bild aus dem Emulator holen
            frame = self.emulator.get_frame()  # Methode zum Abrufen des aktuellen Frames implementieren

            # Bild in Pygame-Oberfläche umwandeln und anzeigen
            surface = pygame.surfarray.make_surface(frame)
            self.screen.blit(surface, (0, 0))
            pygame.display.flip()
