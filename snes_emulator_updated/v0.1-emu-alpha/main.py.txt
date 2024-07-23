import pygame
from snes_emulator.brain.cartridge import Cartridge
from snes_emulator.hands.controller import Controller
from snes_emulator.eyes.display import Display
from memory.brain import Memory
from apu.ears import APU
from cpu.brain import CPU

def main():
    pygame.init()

    # Emulator-Komponenten erstellen
    memory = Memory()
    ppu = PPU(memory)
    apu = APU(memory)
    cpu = CPU(memory, ppu, apu)
    cartridge = Cartridge("roms/som-de.sfc")  # Pfad zur ROM-Datei angepasst
    display = Display()
    controller = Controller()

    # ROM laden
    cartridge.load_rom(memory)

    # Emulationsschleife
    clock = pygame.time.Clock()
    fps = 60  # Ziel-FPS (SNES läuft mit ca. 60 FPS)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                controller.handle_event(event)

        cpu.set_controller_state(controller.get_button_state())
        cpu.execute_instruction()
        ppu.render()
        apu.step()
        display.update(ppu.get_frame())

        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()
