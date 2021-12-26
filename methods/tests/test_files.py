# -*- coding: utf-8 -*-

from methods.files import (
    read_csv,
    save_csv,
    pd_read_csv,
    pd_save_csv,
    read_json,
    save_json,
    read_txt,
    save_txt
)


def test_txt():
    save_txt('save txt')
    print(read_txt('template.txt'))


def test_json():
    save_json({'test': 'json'})
    print(read_json('template.json'))


def test_csv():
    save_csv(['a', 'b'], headers=['x', 'y'])
    print(read_csv('template.csv'))


if __name__ == '__main__':
    test_txt()
    test_json()
    test_csv()
