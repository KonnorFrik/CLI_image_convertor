import pytest
import os


BASE_DIR = "tests_images/"
possible_formats = ['webp', 'png', 'jpeg', 'bmp']
formats_names = [f"from {form}" for form in possible_formats]
###### for ONE ######
#### for exit #######
params_for_one = (('not_exist_file', 'file'),)
params_for_one_ids = ("Fake input",)
#####################
##### for MANY ######
#### for exit #######
params_for_many = (('fake_ext', 'png', 'tests_images', 'tests_images'),
('bmp', 'png', 'fake_dir', 'fake_dir2'),
('not_exist_extension', 'not_exst_ext', 'fake_dir', 'fake_dir2')) #('png', 'fake_ext', 'tests_images', 'tests_images')) # not used

params_for_many_ids = ("Fake input ext",
                       "Fake input dirs",
                       "Fake all",
                       )
#####################


@pytest.fixture(name='tmp_dir_one', scope='session')
def get_tmp_dir(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp("images_one")
    return a_dir


@pytest.fixture(name='tmp_dir_many', scope='session')
def get_tmp_dir_(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp("images_many")
    return a_dir


@pytest.fixture(params=params_for_many, ids=params_for_many_ids, name='manyargs')
def get_args_for_many(request):
    """ Return a data for test 'many'"""
    return request.param


@pytest.fixture(params=params_for_one, ids=params_for_one_ids, name="oneargs")
def get_args_for_one(request):
    """Return a data for test 'one'"""
    return request.param


@pytest.fixture(name="one_names", scope='session')
def get_names_for_one_convert(tmp_dir_one):
    files_before_convert = os.listdir(BASE_DIR)
    files_to_convert = list()

    for file in files_before_convert:
        formats_copy = possible_formats.copy()
        formats_copy.remove(file.split('.')[-1])

        for format_ in formats_copy:
            name_input = BASE_DIR + file
            name_output = str(tmp_dir_one) + '/' + file + '.' + format_
            files_to_convert.append((name_input, name_output))

    yield files_to_convert


@pytest.fixture(name='many_names', params=possible_formats, ids=formats_names)
def get_names_for_many_convert(request, tmp_dir_many):
    data_for_test = list()
    files_before_convert = os.listdir(BASE_DIR)

    format_copy = possible_formats.copy()
    format_copy.remove(request.param)

    for out_format in format_copy:
        files = [file for file in os.listdir(BASE_DIR) if file.split('.')[-1] == request.param]
        files_out = [file.split('.')[0] + '.' + out_format for file in files]
        data_for_test.append((request.param, out_format, BASE_DIR, str(tmp_dir_many), files_out))

    yield data_for_test

