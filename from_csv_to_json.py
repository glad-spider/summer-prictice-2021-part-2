from converter_file_format import Converter
from json import dumps

class CSV_JSON(Converter):

    def __init__(self, file_csv):
        self.nmcsv = file_csv
        self.data_csv = []          #храниние получаемой инфу из файла
        self.open()                 #прочитать файл
        self.data_json = {}         #запись в формате словаря
        self.header_keys = []
        self.read_header()

    def close(self):
        pass

    def open(self):
        with open(self.nmcsv, 'r') as fl:
            for line in fl:
                self.data_csv.append(line.strip('\n'))

        print(self.data_csv)

    def read_header(self):
        self.header_keys = self.data_csv[0].split(',')

    #index - poss cell(column)
    def get_data_column(self, index):
        some_dt = {}
        for line in range(1, len(self.data_csv)):
            some_dt[line] = self.data_csv[line].split(',')[index]

        #print(some_dt)
        return  some_dt

    #key = self.header_keys[i]
    def record_value(self, key, index):
        self.data_json[f'{key}'] = self.get_data_column(index)

    def change_on(self):
        for index in range(len(self.header_keys) - 1):
            self.record_value(key=self.header_keys[index], index=index)

        self.record_to_file()

    def show_result(self):
        self.change_on()

    def record_to_file(self):
        import json
        with open('output.json', 'w') as fl:
            json.dump(self.data_json, fl)


c = CSV_JSON('addresses.csv')
c.show_result()


