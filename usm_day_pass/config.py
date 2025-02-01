from dataclasses import dataclass
from typing import Dict, Any
import os


@dataclass
class Config:
    DATABASE_URI: str
    DATABASE_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    
    @classmethod
    def from_env(cls) -> "Config":
        """Create configuration from environment variables."""
        data: Dict[str, Any] = {}        
        for param in cls.__annotations__.keys():
            if param in os.environ:
                data[param] = os.environ[param]
                    
        return cls(**data)
    
    @property
    def postgres_url(self) -> str:
        """Generate PostgreSQL connection URL."""
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

config = Config.from_env()
