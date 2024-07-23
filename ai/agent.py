from stable_baselines3.common.torch_layers import BaseFeaturesExtractor
import torch.nn as nn

class SecretOfManaAgent(BaseFeaturesExtractor):
    def __init__(self, observation_space, features_dim=256):
        super().__init__(observation_space, features_dim)
        # Hier definierst du die Architektur deines neuronalen Netzes
        self.cnn = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=8, stride=4, padding=0),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=0),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.Flatten(),
        )
        
        # Zusätzliche Layer für die Verarbeitung der Spielinformationen
        self.linear = nn.Sequential(
            nn.Linear(self._features_dim, features_dim),
            nn.ReLU()
        )

    def forward(self, observations):
        # Hier verarbeitest du die Beobachtungen (Spielzustand)
        x = self.cnn(observations)
        return self.linear(x)
