import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

dotenv.load_dotenv(dotenv_path)

class Config:
    @staticmethod
    def GetValue(key: str) -> str:
        env = os.getenv(key)
        if env is None: raise Exception()
        return env