from enum import StrEnum
from typing import Self

from pydantic import BaseModel, DirectoryPath, EmailStr, FilePath, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(StrEnum):
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'
    WEBKIT = 'webkit'


class TestData(BaseModel):
    image_png_file: FilePath


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    traces_dir: DirectoryPath
    browser_state_file: FilePath

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath('./videos')
        traces_dir = DirectoryPath('./traces')
        browser_state_file = FilePath('browser-state.json')

        videos_dir.mkdir(exist_ok=True)
        traces_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            traces_dir=traces_dir,
            browser_state_file=browser_state_file
        )

    def get_base_url(self) -> str:
        return f'{self.app_url}/'


settings = Settings.initialize()
