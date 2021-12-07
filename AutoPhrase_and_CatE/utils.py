# -----------------------------------------------------------------------------------------------------
# UCLA CS 245 Final Project - Seed Based NER
# 
# utils.py is used to process json and text file in preparation for AutoPhrase and CatE mining
#
# (C) 2021 Team NeiJuan, Los Angeles, US
# References:
# https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/version/106 for Covid-19 data
# ------------------------------------------------------------------------------------------------------

import os
import re
import random
import json
# import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
words = stopwords.words('english')

def select_paper(path):
    """
    randomly select 12,000 files from Covid19 dataset

    :param path: path to the Covid19 open research dataset
    :return: a list of json file path, e.g. ["/data/1.json", "/data/2.json", ...]
    """
    file_list = []
    for f in os.listdir(path):
        if f.endswith(".json"):
            subPath = os.path.join(path, f)
            file_list.append(subPath)
    
    selected_articles = []
    # randomly choose 12000 files
    selected_articles.extend(random.sample(file_list, 12000))
    print("Randomly select 12,000 articles.")

    return selected_articles

def extract_text(file_list):
    """
    extract body texts from a list of json file
    in the output txt file, each line is an artilce's body text

    :param file_list: a list of json file path
    :return: a txt file which stores the body text of each article
    """
    f_out = open('raw_text.txt', 'w')
    
    for f in file_list:
        file = open(f, 'r')
        dict = json.load(file)
        body_text = dict["body_text"]
        for section in body_text:
            # extract every paragraph in the body text
            text = section["text"]
            f_out.write(text.strip())
            f_out.write(" ")
        f_out.write("\n")
        file.close()
    f_out.close()
    print("Succesfully extract body texts from json file.")
    # return the raw text file name
    return 'raw_text.txt'

def delete_blank_line(path):
    """
    when some articles have no body text,
    a blank line will be generated in the raw text file.
    Use this function to delete those blank lines in raw text

    :param path: the path to raw text
    :return: raw text without blank lines
    """
    file1 = open(path, 'r')
    file2 = open('res_text2.txt', 'w')
    str = file1.read()
    lst = [line for line in str.split('\n') if line.strip() != '']
    for i in range(len(lst)):
        file2.write(lst[i])
        file2.write('\n') 
    file1.close()
    file2.close()
    return 'res_text2.txt'

def preprocess(path):
    """
    preprocess the raw text file

    :param path: path to the raw text file raw_text.txt
    :return: a clean txt file which stores the body text of each article
    """
    f_in = open(path, 'r')
    text = f_in.read().strip()
    text = text.lower()
    # text = transform(text)
    f_out = open("res_text", 'w')
    f_out.write(text)
    print("Proprocessing raw text done.")
    f_in.close()
    f_out.close()

def remove_stop_words(text_tokens):
    """
    remove stop words from text
    stop words for english are commonly used word such as 'the', 'a', 'an'
    which is not helpful when training models

    :param text_tokens: the text to process
    :return: text without stop words
    """
    temp = []
    for word in text_tokens:
        if word not in words:
            temp.append(word)
    return temp

def remove_non_alpha_character(text_tokens):
    """
    remove special characters, numbers, and punctuation such as '(space)!#%&? etc,.'
    isalpha is true only when word is an alphabet character (a~z)

    :param text: the text to process
    :return: text with only alphabet character
    """
    temp = []
    for word in text_tokens:
        if word.isalpha():
            temp.append(word)
    return temp

def transform(text):
    """
    clean up those extra words including stop words and special characters
    those information doesn't matter a lot

    :param text: the text to process
    :return: a clean text
    """
    text = word_tokenize(text.lower())
    text = remove_stop_words(text)
    text = remove_non_alpha_character(text)
    print("Stop words and special characters have been removed.")
    return ' '.join(text)

def find_seed_index(seed_list_path, raw_text_path):
    """
    find the index of those seed entities in the raw text
    those indices information is prepared for later bond training
    data format:
    for the seed list, each line should be "<category> : seed1 seed2 ..."
    for the raw text, each line is an article
    for the output format, each line is {"body" : "<body_text>", "entities" :
    [{"text": <phrase/word>, "start": <start_index>, "end": <end_index>, "type": <category>}, ...]}

    :param seed_list_path: path to the seed list file
    :param raw_text_path: path to the raw text file
    :return: a json file 
    """
    # dictionary for each category and their seeds
    dict = {}
    file1 = open(seed_list_path, 'r')
    lines = file1.readlines()
    for l in lines:
        segments = l.split(' : ')
        candidates = segments[1].split(' ')
        # replace underscore with space
        output = [c.replace('_', ' ').strip() for c in candidates]
        str_list = list(filter(None, output))
        # match category name to its seeds
        dict[segments[0].upper().replace('_', ' ')] = str_list
    file1.close()

    file2 = open(raw_text_path, 'r')
    file3 = open('indices.json', 'w')
    content = file2.read()
    lines = content.splitlines()
    for l in lines:
        line = l.lower()
        dict2 = {}
        dict2["body"] = l
        dict2["entities"] = []
        for category in dict.keys():
            for item in dict[category]:
                # use re.finditer to find all the occurences of a seed
                indices = [(m.start(), m.end()) for m in re.finditer(item, line)]
                for index in indices:
                    in_dict = {}
                    in_dict["text"] = item
                    in_dict["start"] = index[0]
                    in_dict["end"] = index[1]
                    in_dict["type"] = category
                    dict2["entities"].append(in_dict)
        output = json.dumps(dict2)
        file3.writelines(output)
        file3.write("\n")
    file2.close()
    file3.close()
    print("Index file indices.json generated.")
    return "indices.json"
    
if __name__ == "__main__":
    file_list = select_paper("data")
    file_path = extract_text(file_list)
    # file_path = delete_blank_line(file_path)
    preprocess(file_path)
    # res_path = find_seed_index('seeds.txt', 'raw_text.txt')