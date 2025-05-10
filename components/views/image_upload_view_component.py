from pathlib import Path

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.text import Text


class ImageUploadViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page=page)

        self.preview_empty_view = EmptyViewComponent(page=page, identifier=identifier)
        self.preview_image = Image(page, f'{identifier}-image-upload-widget-preview-image', 'Image preview')
        self.image_upload_info_icon = Icon(page, f'{identifier}-image-upload-widget-info-icon', 'Upload icon')
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text', 'Upload title')
        self.image_upload_info_description = Text(
            page, f'{identifier}-image-upload-widget-info-description-text', 'Upload description'
        )
        self.upload_button = Button(page, f'{identifier}-image-upload-widget-upload-button', 'Upload button')
        self.remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button', 'Remove button')
        self.upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', 'Upload input')

    def assert_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.assert_visible()
        self.image_upload_info_title.assert_visible()
        self.image_upload_info_title.assert_have_text(text='Tap on "Upload image" button to select file')
        self.image_upload_info_description.assert_visible()
        self.image_upload_info_description.assert_have_text(text='Recommended file size 540X300')
        self.upload_button.assert_visible()
        if is_image_uploaded:
            self.preview_image.assert_visible()
            self.remove_button.assert_visible()
        else:
            self.preview_empty_view.assert_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file_path: str | Path):
        self.upload_input.set_input_files(file=file_path, )
