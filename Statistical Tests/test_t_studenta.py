import math, statistics
class tStudent:
    def __init__(self,path,significance, real_value):
        self.path = path
        self.significance = significance
        self.real_value = real_value
        self.data = self.LoadFile()
        self.t_kryt = self.critical_value()
        self.values = self.StudentTest()

    def critical_value(self):
            table = {
                1: {0.5: 1.0000, 0.2: 3.0777, 0.1: 6.3138, 0.05: 12.7062, 0.02: 31.8205, 0.01: 63.6567, 0.0005: 127.3213, 0.002: 318.3088, 0.001: 636.6192},
                2: {0.5: 0.8165, 0.2: 1.8856, 0.1: 2.9200, 0.05: 4.3029, 0.02: 6.9646, 0.01: 9.9246, 0.0005: 14.0890, 0.002: 22.3271, 0.001: 31.5991},
                3: {0.5: 0.7649, 0.2: 1.6377, 0.1: 2.3534, 0.05: 3.1824, 0.02: 4.5407, 0.01: 5.8409, 0.0005: 7.4543, 0.002: 10.2145, 0.001: 12.9240},
                4: {0.5: 0.7407, 0.2: 1.5332, 0.1: 2.1318, 0.05: 2.7764, 0.02: 3.7469, 0.01: 4.5041, 0.0005: 5.5976, 0.002: 7.1732, 0.001: 8.6103},
                5: {0.5: 0.7267, 0.2: 1.4759, 0.1: 2.0150, 0.05: 2.5706, 0.02: 3.3649, 0.01: 4.0321, 0.0005: 4.7733, 0.002: 5.8934, 0.001: 5.8688},
                6: {0.5: 0.7176, 0.2: 1.4398, 0.1: 1.9432, 0.05: 2.4469, 0.02: 3.1427, 0.01: 3.7074, 0.0005: 4.3158, 0.002: 5.2076, 0.001: 5.9688},
                7: {0.5: 0.7111, 0.2: 1.4190, 0.1: 1.8946, 0.05: 2.3646, 0.02: 2.9980, 0.01: 3.4995, 0.0005: 4.0293, 0.002: 4.7853, 0.001: 5.4079},
                8: {0.5: 0.7064, 0.2: 1.3968, 0.1: 1.8595, 0.05: 2.3060, 0.02: 2.8965, 0.01: 3.3554, 0.0005: 3.8325, 0.002: 4.5008, 0.001: 5.0413},
                9: {0.5: 0.7027, 0.2: 1.3830, 0.1: 1.6331, 0.05: 2.2622, 0.02: 2.8214, 0.01: 3.2498, 0.0005: 3.6897, 0.002: 4.2968, 0.001: 4.7809},
                10: {0.5: 0.6998, 0.2: 1.3722, 0.1: 1.8125, 0.05: 2.2281, 0.02: 2.7638, 0.01: 3.1693, 0.0005: 3.5814, 0.002: 4.1437, 0.001:4.5869},
            }
            return round((table[len(self.data)-1][self.significance]),6)


    def LoadFile(self): # Program wysypuje sie kiedy w linii jest co innego niz liczby (puste linie, literki)
        with open(self.path,'r') as f:
            data = [float(line.strip().replace(',','.')) for line in f]
        return data
    
    def StudentTest(self):
         data = self.data.copy()
         comparison = False
         sum = 0
         for i in data: sum+=i
         sred = sum/len(data)
         stdev = statistics.stdev(data)
         t = abs(sred - self.real_value)*math.sqrt(len(data))/stdev
         if t > self.t_kryt: comparison = True
         values = [sred,stdev,t,comparison]
         return values
         
    def Show_Info(self):
        print('test t studenta'.upper().center(60))
        print('='*60)
        print(f'Sciezka do pliku:\t {self.path}')
        print(f'Ilosc elementow w serii: {len(self.data)}')
        print(f'Ufnosc:\t\t\t {self.significance}')
        print(f'Wartosc sredniej:\t {self.values[0]}')
        print(f'Wartosc odchylenia standardowego:\t {round(self.values[1],8)}')
        print(f'Wartosc t_kryt.:\t {self.t_kryt}')
        print(f'Wartosc t:\t {round(self.values[2],6)}')
        print(f'Czy t > t_kryt:\t {self.values[3]}')
        if self.values[3] == True: print('Wyniki roznia sie na poziomie statystycznie istotnym!')
        else: print('Wyniki nie roznia sie na poziomie statystycznie istotnym!')
        print('='*60)

    def Export_to_file(self,path_to_export):
        with open(path_to_export,'a') as file:
            file.write('test t Studenta'.upper().center(60) + '\n')
            file.write('='*60 + '\n')
            file.write(f'Sciezka do pliku:\t {self.path}\n')
            file.write(f'Ilosc elementow w serii: {len(self.data)}\n')
            file.write(f'Ufnosc:\t\t\t {self.significance}\n')
            file.write(f'Wartosc sredniej:\t {self.values[0]}\n')
            file.write(f'Wartosc odchylenia standardowego:\t {round(self.values[1],8)}\n')
            file.write(f'Wartosc t_kryt.:\t {self.t_kryt}\n')
            file.write(f'Wartosc t:\t {round(self.values[2],6)}\n')
            file.write(f'Czy t > t_kryt:\t {self.values[3]}\n')
            if self.values[3] == True: file.write('Wyniki roznia sie na poziomie statystycznie istotnym!\n')
            else: file.write('Wyniki nie roznia sie na poziomie statystycznie istotnym!\n')
            file.write('='*60 + '\n')

