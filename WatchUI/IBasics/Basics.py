import os
from robot.api import logger


class Basics:
    save_folder_path = "../Outputs"
    ssim_basic = 1.5
    starts_format_image = "png"
    path_to_tesseract_folder = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def check_dir(self, save_folder: str) -> str:
        if save_folder != self.save_folder_path:
            os.mkdir(save_folder)
            self.save_folder_path = save_folder
        else:
            if not os.path.exists(self.save_folder_path):
                os.mkdir(self.save_folder_path)
        return self.save_folder_path

    def check_image_exists(self, path: str) -> None:
        if not os.path.exists(path):
            raise AssertionError("The path: %s, to the image does not exist." % path)

    def check_ssim(self, ssim: float) -> float:
        if ssim == 1.0:
            return float(self.ssim_basic)
        else:
            return float(ssim)

    def check_image_format(self, format: str) -> str:
        if str(format) == 'png':
            self.format = '.' + self.starts_format_image
        else:
            self.format = '.' + format
        return self.format

    def check_tess_path(self, path_to_tess: str) -> str:
        if path_to_tess == r'C:\Program Files\Tesseract-OCR\tesseract.exe':
            tess_way = self.path_to_tesseract_folder
        else:
            tess_way = path_to_tess
        return tess_way

    def set_log_message(self, work_object="Image", type_of_messages="Info", path_to_image=""):
        if work_object == "Image":
            if type_of_messages == "Info":
                logger.info("Image was saved to your output folder </p><img src='" + path_to_image + "'/>", html=True)
            elif type_of_messages == "Error":
                logger.error("Images arent same</p><img src='" + path_to_image + "'/>", html=True)
        elif work_object == "PDF":
            pass
        elif work_object == "Tesseract":
            pass
        else:
            logger.warn("!!! Bad work object !!! Please contact library owner...", html=True)

    def check_if_args_has_ok_numbers(self, *args, need_numbers=4):
        nArg = len(args)
        if nArg % need_numbers == 0:
            True
        else:
            logger.error("You try to set bad numbers of arguments. You need %s arguments" % need_numbers, html=False)
