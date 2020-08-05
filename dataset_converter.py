import json
import logging
import sys

try:
    f = open("NER_test_BILOU.tsv", 'r')
    fwords = open("model.words.txt", 'w')
    ftags = open("model.tags.txt", 'w')
    labels = []
    s = ''
    for line in f:
        if line[0:len(line) - 1] != '.\tO':
            try:
                word, entity = line.split('\t')
            except ValueError:
                continue
            s += word + " "
            entity = entity[:len(entity) - 1]
            labels.append(entity)
        else:
            fwords.write(s)
            fwords.write('\n')
            s = ''
            labels_str = ''
            for label in labels:
                labels_str += label + " "
            ftags.write(labels_str)
            ftags.write('\n')
            labels = []
except Exception as e:
    logging.exception("Unable to process file" + "\n" + "error = " + str(e))