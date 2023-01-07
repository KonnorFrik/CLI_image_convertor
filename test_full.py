from main import convert_many, convert_one
import os
import pytest


BASE_DIR = "tests_images/"


@pytest.mark.convert
def test_convert_one(one_names):
    for name_input, name_output in one_names:
        convert_one(name_input, name_output)
        assert os.path.exists(name_output)


@pytest.mark.convert
def test_convert_many(many_names):
        for ext_from, ext_to, dir_in, dir_out, files_out in many_names:
            convert_many(ext_from=ext_from, ext_to=ext_to, dir_in=dir_in, dir_out=dir_out)
            list_dir = os.listdir(dir_out)
            assert all([file in list_dir for file in files_out])


class TestExit:
    @pytest.mark.typeerr
    def test_one_for_typeerr(self):
        with pytest.raises(TypeError):
            convert_one()

    @pytest.mark.typeerr
    def test_many_for_typeerr(self):
        with pytest.raises(TypeError):
            convert_many()

    @pytest.mark.filenotfounderr
    def test_one_for_exit(self, oneargs):
        #print(oneargs)
        with pytest.raises(FileNotFoundError):
            convert_one(*oneargs)

    @pytest.mark.filenotfounderr
    def test_many_for_exit(self, manyargs):
        #print(myargs)
        with pytest.raises(FileNotFoundError):
            convert_many(*manyargs)

    #def test_fake_output_ext_many(self):
        #with pytest.raises(Exception):
            #convert_many()
