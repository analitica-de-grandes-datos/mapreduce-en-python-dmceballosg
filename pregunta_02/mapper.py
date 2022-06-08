#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import fileinput
import glob
import os
import string 
from multiprocessing import Pool
from toolz.functoolz import compose
from toolz.itertoolz import concat

# -------------------------------- Utils --------------------------------
def tolower(x):
    return x.lower()

def remove_punctuation(x):
    return x.translate(str.maketrans("", "", string.punctuation))

def remove_newline(x):
    return x.replace("\n", "")

def split_lines(x):
    return x.split(',')

def create_purpose_amount(x):
    return x[3] + "*" + x[4]
# -------------------------------- End Utils --------------------------------
# ------------------------------ Mapper -------------------------------------
class Mapper:
    def __init__(self, input_stream):
        self.file_path = input_stream

    def load_data(self):
        def make_iterator_from_single_file():
            with open(self.file_path, "rt") as file:
                for line in file:
                    yield line

        def make_iterator_from_multiple_files():
            file_path = os.path.join(self.file_path, "*")
            files = glob.glob(file_path)
            with fileinput.input(files=files) as file:
                for line in file:
                    yield line

        if os.path.isfile(self.file_path):
            return make_iterator_from_single_file()
        return make_iterator_from_multiple_files()
        
# ------------------------------ END Mapper --------------------------------

compose_pipeline = compose(
    create_purpose_amount,
)

with Pool() as pool:
    mapper = Mapper("credit.csv")
    result = pool.map(split_lines, mapper.load_data())
    result = pool.map(compose_pipeline, result)

for line in list(result):
    print(line)