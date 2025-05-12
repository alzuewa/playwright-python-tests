import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page, Playwright


def initialize_playwright_page(playwright: Playwright, test_name: str, storage_state: str | None = None) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(record_video_dir='./videos', storage_state=storage_state)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    trace_report_path = f'./traces/{test_name}.zip'
    context.tracing.stop(path=trace_report_path)
    browser.close()

    allure.attach.file(source=trace_report_path, name='playwright_trace', extension='zip')
    allure.attach.file(source=page.video.path(), name='playwright_video', attachment_type=AttachmentType.WEBM)
