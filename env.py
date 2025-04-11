import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')


class Config:
    @staticmethod
    def GetValue(key: str) -> str:
        dotenv.load_dotenv(dotenv_path)
        env = os.getenv(key)
        if env is None: raise Exception()
        return env