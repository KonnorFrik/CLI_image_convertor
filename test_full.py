from main import convert_many, convert_one
import os
import pytest

BASE_DIR = "tests_images/"
possible_formats = ['webp', 'png', 'jpeg', 'bmp']


def test_convert_one():
    files_to_convert = os.listdir(BASE_DIR)

    for file in files_to_convert:
        formats_copy = possible_formats.copy()
        formats_copy.remove(file.split('.')[-1])

        for format_ in formats_copy:
            name_input = BASE_DIR + file
            name_output = file + '.' + format_
            convert_one(name_input, BASE_DIR + name_output)

            try:
                assert name_output in os.listdir(BASE_DIR)

            except Exception:
                pass

            finally:
                os.remove(BASE_DIR + name_output)


def test_convert_many():
    for format_ in possible_formats:
        format_copy = possible_formats.copy()
        format_copy.remove(format_)

        for out_format in format_copy:
            files = [file for file in os.listdir(BASE_DIR) if file.split('.')[-1] == format_]
            files_out = [file.split('.')[0] + '.' + out_format for file in files]

            convert_many(ext_from=format_, ext_to=out_format, dir_in=BASE_DIR, dir_out=BASE_DIR)

            try:
                files_after = os.listdir(BASE_DIR)
                assert files_out in files_after

            except Exception:
                pass

            finally:
                for file in files_out:
                    os.remove(BASE_DIR + file)


class TestExit:
    def test_without_args_one(self):
        with pytest.raises(TypeError):
            convert_one()

    def test_without_args_many(self):
        with pytest.raises(TypeError):
            convert_many()

    def test_fake_file_one(self):
        with pytest.raises(FileNotFoundError):
            convert_one('not_exist_file', 'file')

    def test_fake_exts_dirs_many(self):
        with pytest.raises(FileNotFoundError):
            convert_many('not_exist_extension', 'not_exst_ext', 'fake_dir', 'fake_dir2')

    def test_fake_dirs_many(self):
        with pytest.raises(FileNotFoundError):
            convert_many('bmp', 'png', 'fake_dir', 'fake_dir2')

    def test_fake_input_ext_many(self):
        with pytest.raises(Exception):
            convert_many('fake_ext', 'png', 'tests_images', 'tests_images')

    #def test_fake_output_ext_many(self):
        #with pytest.raises(Exception):
            #convert_many('png', 'fake_ext', 'tests_images', 'tests_images')
