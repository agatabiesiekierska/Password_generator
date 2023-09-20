class DixonTest:
    def __init__(self,path,significance):
        self.path_to_imp = path
        self.significance = significance
        self.data = self.LoadFile()
        self.q_kryt = self.critical_value()
        self.values = self.Dixon()
        self.compare = self.Comparison()

    def critical_value(self):
            table = {
                3: {0.90: 0.941, 0.95: 0.970, 0.99: 0.994,},
                4: {0.90: 0.765, 0.95: 0.829, 0.99: 0.926,},
                5: {0.90: 0.642, 0.95: 0.710, 0.99: 0.821,},
                6: {0.90: 0.560, 0.95: 0.625, 0.99: 0.740,},
                7: {0.90: 0.507, 0.95: 0.568, 0.99: 0.680,},
                8: {0.90: 0.468, 0.95: 0.526, 0.99: 0.634,},
                9: {0.90: 0.437, 0.95: 0.493, 0.99: 0.598,},
                10: {0.90: 0.412, 0.95: 0.466, 0.99: 0.568,},
            }
            return round((table[len(self.data)][self.significance]),6)

    def LoadFile(self): # Program wysypuje sie kiedy w linii jest co innego niz liczby (puste linie, literki)
        with open(self.path_to_imp,'r') as f:
            data = [float(line.strip().replace(',','.')) for line in f]
        return data

    def Dixon(self):
        while len(self.data) >= 3:
            try:    
                data_sorted = sorted(self.data)
                r = max(self.data) - min(self.data)
                q1 = (data_sorted[1]-data_sorted[0])/r
                qn = (data_sorted[len(self.data)-1]-data_sorted[len(self.data)-2])/r
                values = [round(q1,6),round(qn,6)]
                return values
            except: return None
        else: print('To less elements to perform the test!')

    def Comparison(self):
        val = ['MIN', 'MAX']
        list_compare = []
        for i,j in zip(self.values, val):
            if i > self.q_kryt:
                compare = f'Nalezy odrzucic wartosc {j}'
            else: compare = f'Nie nalezy odrzucac wartosci {j}'
            list_compare.append(compare)
        return list_compare

    def Show_Info(self):
        print('test q dixona'.upper().center(60))
        print('='*60)
        print(f'Sciezka do pliku:\t {self.path_to_imp}')
        print(f'Ilosc elementow w serii: {len(self.data)}')
        print(f'Ufnosc:\t\t\t {self.significance}')
        print(f'Wartosc Q_kryt.:\t {self.q_kryt}')
        print(f'Wartosc rozstepu:\t {round((max(self.data) - min(self.data)),6)}')
        print(f'Wartosc Q1 i Qn:\t {self.values}')
        for i in self.compare: print(i)
        print('='*60)


    def Export_to_file(self,path_to_export):
        with open(path_to_export,'a') as file:
            file.write('test q dixona'.upper().center(60) + '\n')
            file.write('='*60 + '\n')
            file.write(f'Sciezka do pliku:\t {self.path_to_imp}\n')
            file.write(f'Ilosc elementow w serii: {len(self.data)}\n')
            file.write(f'Ufnosc:\t\t\t {self.significance}\n')
            file.write(f'Wartosc Q_kryt.:\t {self.q_kryt}\n')
            file.write(f'Wartosc rozstepu:\t {round((max(self.data) - min(self.data)),6)}\n')
            file.write(f'Wartosc Q1 i Qn:\t {self.values}\n')
            for i in self.compare: file.write(f'{i}\n')
            file.write('='*60 + '\n')
            
