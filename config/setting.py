import os
from dataclasses import dataclass, field
from typing import List
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    SECRET_KEY: str = field(default_factory=lambda: os.getenv('SECRET_KEY', 'your-secret-key'))
    DEBUG: bool = field(default_factory=lambda: os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 'yes'])
    
    # API Keys
    GROQ_API_KEY: str = field(default_factory=lambda: os.getenv('GROQ_API_KEY'))
    DEEPSEEK_API_KEY: str = field(default_factory=lambda: os.getenv('DEEPSEEK_API_KEY'))
    
    # API Models
    GROQ_MODEL: str = field(default_factory=lambda: os.getenv('GROQ_MODEL', 'mixtral-8x7b-32768'))
    DEEPSEEK_MODEL: str = field(default_factory=lambda: os.getenv('DEEPSEEK_MODEL', 'deepseek-chat'))
    DEEPSEEK_BASE_URL: str = field(default_factory=lambda: os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com'))
    
    # Analysis Settings
    ANALYSIS_ENGINE: str = field(default_factory=lambda: os.getenv('ANALYSIS_ENGINE', 'hybrid'))
    CACHE_TTL: int = field(default_factory=lambda: int(os.getenv('CACHE_TTL', '1800')))  # 30 minutes
    RATE_LIMIT_PER_MINUTE: int = field(default_factory=lambda: int(os.getenv('RATE_LIMIT_PER_MINUTE', '60')))
    ALLOWED_ORIGINS: List[str] = field(default_factory=lambda: os.getenv('ALLOWED_ORIGINS', '*').split(','))
    
    # Advanced Analysis Settings
    MIN_CONFIDENCE_THRESHOLD: float = field(default_factory=lambda: float(os.getenv('MIN_CONFIDENCE_THRESHOLD', '0.7')))
    MAX_LOG_SIZE: int = field(default_factory=lambda: int(os.getenv('MAX_LOG_SIZE', '100000')))
    ENABLE_BEHAVIORAL_ANALYSIS: bool = field(default_factory=lambda: os.getenv('ENABLE_BEHAVIORAL_ANALYSIS', 'True').lower() in ['true', '1', 'yes'])
    
    @classmethod
    def validate(cls) -> bool:
        instance = cls()
        if not instance.GROQ_API_KEY and not instance.DEEPSEEK_API_KEY:
            print("Error: At least one API key (GROQ_API_KEY or DEEPSEEK_API_KEY) is required")
            return False
        
        valid_engines = ['groq', 'deepseek', 'hybrid']
        if instance.ANALYSIS_ENGINE not in valid_engines:
            print(f"Error: ANALYSIS_ENGINE must be one of: {valid_engines}")
            return False
        return True

config = Config()
