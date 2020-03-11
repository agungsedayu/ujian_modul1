# UJIAN MODUL ! TANGGAl 11 MARET 2020 

#SOAL NOMOR 1 

#  def hashtag():
#     kata = input('Masukkan kata: ')
#     z = ''
#     for i in kata.split():
#         z += i.capitalize()
#         # print(z)
#     if len(z) > 140 or len(z) == 0:
#         print(False)
#     else:
#         print('#'+z)

# hashtag()

# Hashtag(" Hello there how are you doing")   #HelloThereHowAreYouDoing"

###########################################################
#SOAL NOMOR 2

# def create_phone_number():
#     number = input('Input number:')
#     z = []
#     for i in list(number):
#         z += [i]
#     # return z
#     print('({}{}{}) {}{}{}-{}{}{}{}'.format(z[0], z[1], z[2], z[3], z[4], z[5], z[6], z[7], z[8], z[9]))

# create_phone_number()

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])  "(123) 456-7890" 

########################################################
#SOAL NOMOR 3

def Sort_odd_even(number):
    idxodd = []
    valodd = []
    idxeven = []
    valeven = []
    for idx, val in enumerate(number):
        if val %2 != 0:
            idxodd.append(idx)
            valodd.append(val)
        else:
            idxeven.append(idx)
            valeven.append(val)
    # print(idxodd)
    # print(valodd)
    # print(idxeven)
    # print(valeven)
            
    #ascendingODD
    for i in range(len(valodd)):
        for j in range(i+1, len(valodd)):
            if valodd[i] > valodd[j]:
                valodd[i], valodd[j] = valodd[j], valodd[i]
    # print(valodd)

    #descendingEVEN
    for i in range(len(valeven)):
        for j in range(i+1, len(valeven)):
            if valeven[i] < valeven[j]:
                valeven[i], valeven[j] = valeven[j], valeven[i]
    # print(valeven)
    sort = valodd + valeven
    print(sort)


Sort_odd_even([5, 3, 2, 8, 1, 4])  #[1, 3, 8, 4, 5, 2] 

############################################################
#SOAL NOMOR 4

# def hollowtriangle(n):
#     if n == 1:
#         print('#')
#         return False
    
#     atas = ['_' * (n-1) + '#' + '_' * (n-1)]
#     tengah = []
#     bawah = ['#'*((2*n)-1)]

#     for i in range(n-2,0,-1):
#         tengah.append(('_'*i) + '#' + ('_' * ((2*n)-(2*i)-3))+'#'+('_'*i))
#         print(atas[0])
    
#     for i in tengah:
#         print(i)

#     print(bawah[0])

# hollowtriangle(6)