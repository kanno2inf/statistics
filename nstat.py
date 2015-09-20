#!/usr/bin/python
# -*- encoding:utf-8 -*-
import argparse
import itertools
import sys
import statistics


def encoding_out():
    return sys.stdout.encoding or sys.getfilesystemencoding()


def encoding_in():
    return sys.stdin.encoding or sys.getfilesystemencoding()


def read_data(file_path):
    with open(file_path, "r") as f:
        return [line.split() for line in f if line.strip()]


def eval_corr(v1, v2):
    return statistics.eval_correlation(statistics.correlation(v1, v2)).encode(encoding_out())


if __name__ == "__main__":
    # Shift-JIS, tsvのみ対応
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE', help=u'tab split file. need all columns.')
    parser.add_argument('-e', '--eval', action="store_true", help=u'correlation value to evaluation text.')
    parser.add_argument('-d', '--delimiter', metavar='DELIMITER', default='\t', help=u'output delimiter.')
    opt = parser.parse_args()

    # ファイルから読み込み
    data = read_data(opt.file.decode(encoding_in()))
    columns = data[0]
    # 列名毎のリストにする
    data = map(list, zip(*data[1:]))
    # 列名毎にベクトルを辞書にまとめる
    data_set = dict(zip(columns[1:], data[1:]))

    names = data_set.keys()
    print opt.delimiter.join(['-'] + names)
    for y in names:
        if opt.eval:
            # 可視化
            records = [y] + ['-' if x == y else eval_corr(data_set[y], data_set[x]) for x in names]
        else:
            # 相関係数
            records = [y] + ['1' if x == y else str(statistics.correlation(data_set[y], data_set[x])) for x in names]
        print opt.delimiter.join(records)
