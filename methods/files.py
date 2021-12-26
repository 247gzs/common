# -*- coding: utf-8 -*-
import codecs
import csv
import json

import pandas as pd

from methods.exceptions import MethodException


def read_csv(filename: str) -> list:
    fr = csv.reader(codecs.open(filename, 'r'))
    row_list = []
    for row in fr:
        row_list.append(row)
    return row_list


def save_csv(rows: list, filename='template.csv', headers=None) -> None:
    writer = csv.writer(codecs.open(filename, 'w'))
    if headers:
        writer.writerow(headers)
    for row in rows:
        writer.writerow(row)


def pd_read_csv(filename: str, **kwargs) -> pd.DataFrame:
    return pd.DataFrame(filename, **kwargs)


def pd_save_csv(df: pd.DataFrame, filename='template.csv', **kwargs) -> None:
    df.to_csv(filename, **kwargs)


def read_json(filename: str) -> dict:
    with codecs.open(filename, 'r') as fr:
        return json.load(fr)


def save_json(row: dict, filename='template.json', indent=2, ensure_ascii=True, **kwargs) -> None:
    with codecs.open(filename, 'w') as fw:
        content = json.dumps(row, indent=indent, ensure_ascii=ensure_ascii, **kwargs)
        fw.write(f'{content}')


def read_txt(filename: str, mode='r', encoding='utf-8', errors='ignore') -> list:
    row_list = []
    with codecs.open(filename, mode=mode, encoding=encoding, errors=errors) as fr:
        for line in fr.readlines():
            line = line.strip()
            if not line:
                continue
            row_list.append(line)
    return row_list


def save_txt(row, filename='template.txt', mode='w', encoding='utf-8', errors='ignore') -> None:
    if not isinstance(row, (str, list)):
        raise MethodException('待保存内容不合法')
    if isinstance(row, str):
        row = [row]
    with codecs.open(filename, mode=mode, encoding=encoding, errors=errors) as fw:
        for line in row:
            fw.write(f'{line}\n')
