import view
import export
import data_writing


def choice():
    some_str = view.inp()
    if some_str == '0':
        data_writing.writing_txt(data_writing.get_info())
    elif some_str == '1':
        view.view_data(export.from_file())
    else:
        view.view_data('Неверный ввод')
