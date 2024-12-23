import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline().strip()

            if not line:
                break

        all_data.append(line)

if __name__ == '__main__':

   filenames = [f'./file {number}.txt' for number in range(1, 5)]
   start_1 = datetime.datetime.now()
   for filename in filenames:
       read_info(filename)

   end_1 = datetime.datetime.now()
   line_result = end_1 - start_1
   print(f'Время работы линейного подхода: {line_result}')



   start_2 = datetime.datetime.now()
   with multiprocessing.Pool(processes=4) as pool:
       pool.map(read_info, filenames)
   end_2 = datetime.datetime.now()
   multiprocessing_result = end_2 - start_2
   print(f'Время работы мультипроцессорного подхода: {multiprocessing_result}')


