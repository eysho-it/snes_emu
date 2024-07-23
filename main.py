import gym
from stable_baselines3 import PPO
from ai.agent import SecretOfManaAgent
from ai.emulator_interface import LakeSnesInterface

# Emulator-Schnittstelle erstellen
env = LakeSnesInterface(rom_path="Secret_of_Mana_(Germany).smc")

# KI-Agenten erstellen (mit PPO-Algorithmus)
model = PPO(SecretOfManaAgent, env, verbose=1)

# KI trainieren
model.learn(total_timesteps=1000000)

# Trainiertes Modell speichern
model.save("data/models/ppo_secret_of_mana")

# Spiel mit trainierter KI ausführen und anzeigen
obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()  # Spielbildschirm anzeigen
    