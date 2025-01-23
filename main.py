def main():

   grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
   students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
   aver_scor = []
   stud_sort = list(students)
   stud_sort.sort()
   for i in grades:
       a = sum(i) / len(i)
       aver_scor.append(a)
   av_sc = dict(zip(stud_sort, aver_scor ))
   print(av_sc)

if __name__ == '__main__':
    main()

