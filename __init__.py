from .get_gifNimage import get_gifNimage
print('def get_gifNimage(link, file_name_show=False, dict_appearance=False, show_error_logs=False, only_picture_name=False, markdown_name=False, menu=False, more_info=False)')

"""
For unknown reason when I rename CHANGELOG.TXT to CHANGELOG.md -
 it can't find the file when I try to install the module in Jupyter Notebook.
 I tried to use the code below but without a success. At this point, I will live CHANGELOG.txt version.
"""
# import logging
# try:
#     open('CHANGELOG.md').read()
# except FileNotFoundError as fnfe:
#     logging.exception('Caught an error [in code used: except FileNotFoundError]' + str(fnfe))
#     print('Caught an error [in code used: except FileNotFoundError]')
