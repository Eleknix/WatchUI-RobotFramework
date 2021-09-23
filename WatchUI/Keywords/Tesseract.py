# pylint: disable=invalid-name, no-member, too-many-arguments, too-many-locals
"""Module representing Tesseract class.
"""

import os
from typing import Any, Union

import cv2 as cv
import pytesseract
from WatchUI.IBasics.Basics import Basics


class Tesseract(Basics):
    """Class representing Tesseract and its methods.
    This class is not instantiated itself, but inherited into main WatchUI module class.

    Args:
        Basics (object): interface class
    """

    def create_image_to_string(
        self, path: str, oem: str, psm: str, language: str, path_to_tesseract: str
    ) -> Union[bytes, str]:
        """Converts provided image to string and returns.

        Args:
            path (str): path to the image
            oem (str): [description]
            psm (str): [description]
            language (str): [description]
            path_to_tesseract (str): path to installed tesseract binary

        Returns:
            str: OCRed text from image
        """
        self.check_image_exists(path)

        old_img: Any = cv.imread(path)
        pytesseract.pytesseract.tesseract_cmd = self.check_tess_path(path_to_tesseract)
        custom_oem_psm_config: str = rf"--oem {oem} --psm {psm}"

        text: Union[bytes, str] = pytesseract.image_to_string(
            old_img, config=custom_oem_psm_config, lang=language
        )
        return text

    def create_image_area_on_text(
        self,
        path: str,
        *coordinates,
        oem: str,
        psm: str,
        language: str,
        path_to_tesseract: str,
    ) -> Union[list[str], str]:
        """Convert to text only the selected area of the image and return.

        Args:
            path (str): path to the image
            oem (str): [description]
            psm (str): [description]
            language (str): [description]
            path_to_tesseract (str): path to the installed tesseract library

        Returns:
            Union[list[str], str]: returned text
        """
        string_list = []
        text: Union[bytes, str]
        old_img: Any = cv.imread(path)
        len_coordinates: int = len(coordinates)

        self.check_if_args_has_ok_numbers(*coordinates, need_numbers=4)
        if len_coordinates / 4 == 1:
            crop_img: Any = old_img[
                int(coordinates[1]) : int(coordinates[3]),
                int(coordinates[0]) : int(coordinates[2]),
            ]
            pytesseract.pytesseract.tesseract_cmd = self.check_tess_path(
                path_to_tesseract
            )
            custom_oem_psm_config: str = rf"--oem {oem} --psm {psm}"
            text = pytesseract.image_to_string(
                crop_img, config=custom_oem_psm_config, lang=language
            )
            if not isinstance(text, str):
                raise TypeError(
                    "Tesseract OCRed image and returned data as bytes. We need <str> type."
                )
            stripped_text: str = os.linesep.join(
                [s for s in text.splitlines() if s]
            )  # delete blank line space
            return stripped_text

        num_coordinates: float = len_coordinates / 4
        a: int = 0
        i: int = 0
        while i < num_coordinates:
            x1 = coordinates[0 + a]
            y1 = coordinates[1 + a]
            x2 = coordinates[2 + a]
            y2 = coordinates[3 + a]
            crop_img = old_img[int(y1) : int(y2), int(x1) : int(x2)]
            pytesseract.pytesseract.tesseract_cmd = self.check_tess_path(
                path_to_tesseract
            )
            custom_oem_psm_config = rf"--oem {oem} --psm {psm}"
            text = pytesseract.image_to_string(
                crop_img, config=custom_oem_psm_config, lang=language
            )
            if not isinstance(text, str):
                raise TypeError(
                    "Tesseract OCRed image and returned data as bytes. We need <str> type."
                )

            string_list.append(text)
            i += 1
            a += 4
        return string_list
