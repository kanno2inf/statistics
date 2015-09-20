#!/usr/bin/python
# -*- encoding:utf-8 -*-
import argparse
import itertools
import sys
from nstat import read_data, encoding_in, eval_corr
import statistics


def dataset(fields):
    columns = fields[0]
    # 列名毎のリストにする
    data = map(list, zip(*fields[1:]))
    # 列名毎にベクトルを辞書にまとめる
    return dict(zip(columns[1:], data[1:]))


if __name__ == "__main__":
    # Shift-JIS, tsvのみ対応
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE', nargs=2, help=u'tab split file. need all columns.')
    parser.add_argument('-e', '--eval', action="store_true", help=u'correlation value to evaluation text.')
    parser.add_argument('-d', '--delimiter', metavar='DELIMITER', default='\t', help=u'output delimiter.')
    opt = parser.parse_args()

    # ファイルから読み込み
    data_set1 = dataset(read_data(opt.file[0].decode(encoding_in())))
    data_set2 = dataset(read_data(opt.file[1].decode(encoding_in())))

    keys1 = data_set1.keys()
    keys2 = data_set2.keys()
    print opt.delimiter.join(['-'] + keys2)
    for y in keys1:
        if opt.eval:
            # 可視化
            records = [y] + ['-' if x == y else eval_corr(data_set1[y], data_set2[x]) for x in keys2]
        else:
            # 相関係数
            records = [y] + ['1' if x == y else str(statistics.correlation(data_set1[y], data_set2[x])) for x in keys2]
        print opt.delimiter.join(records)
