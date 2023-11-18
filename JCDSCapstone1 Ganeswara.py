from tabulate import tabulate

#Custom input functions
#Integer input
def IntInput(Teks=''):
    while True:
        try:
            Raw=input(Teks)
            Int=int(Raw)
        except ValueError:
            print('Masukkan bilangan bulat.')
        else:
            return Int

#Float input
def FloatInput(Teks=''):
    while True:
        try:
            Raw=input(Teks)
            Float=float(Raw)
        except ValueError:
            print('Masukkan bilangan.')
        else:
            return Float

#Input for constrained options
def OptInput(Options,Teks=''):
    while True:
        Input=input(Teks)
        if Input in Options:
            return Input
        print('Pilihan tidak tersedia.')
    
#Main menu
def MainMenu(Data,Tags):
    while True:
        print('\nFitur:\n1. Lihat data\n2. Buat data baru\n3. Ubah data\n4. Hapus data\n5. Buat field baru\n6. Urut data\n7. Keluar')
        Opt=OptInput(list(MainMenuOpts)+['7'],'Pilihan menu: ')
        if Opt=='7':
            break
        elif Opt in MainMenuOpts:
            MainMenuOpts[Opt](Data,Tags)
        else:
            print('Pilihan tidak tersedia.')

#Read data menu
def ReadMenu(Data,Tags):
    while True:
        print('\n1. Lihat semua data\n2. Cari data\n3. Kembali ke menu utama')
        Opt=OptInput(['1','2','3'],'Pilihan perintah: ')
        if Opt=='1':
            ReadAll(Data,Tags)
        elif Opt=='2':
            ReadData(Data,Tags)
        elif Opt=='3':
            break

#Show all data
def ReadAll(Data,Tags):
    if len(Data)==0:
        print('Data Kosong.')
    else:
        print('\n',tabulate(Data,headers=Tags['Header']))

#$how 1 data
def ReadData(Data,Tags):
    if len(Data)==0:
        print('Data kosong.')
        return None
    Key=IntInput('Masukkan ID peminjaman yang dicari: ')
    if Key in Tags['PrimeKeys']:
        k=Tags['PrimeKeys'].index(Key)
        print('\n',tabulate([Data[k]],headers=Tags['Header']))
    else:
        print('Data tidak ditemukan.')

#Create data menu
def CreateMenu(Data,Tags):
    while True:
        print('\n1. Tambah data baru\n2. Kembali ke menu utama')
        Opt=OptInput(['1','2'],'Pilihan perintah: ')
        if Opt=='1':
            AddData(Data,Tags)
        elif Opt=='2':
            break

#Add new data
def AddData(Data,Tags):
    NewID=IntInput('\nMasukkan ID peminjaman baru: ')
    if NewID in Tags['PrimeKeys']:
        print('Data dengan ID {} sudah ada.'.format(NewID))
        return None
    NewData=[NewID]
    for i in range(1,len(Tags['Header'])):
        if Tags['Type'][i]==str:
            NewData.append(input('{}: '.format(Tags['Header'][i])).capitalize())
        elif Tags['Type'][i]==int:
            NewData.append(IntInput('{}: '.format(Tags['Header'][i])))
        elif Tags['Type'][i]==float:
            NewData.append(FloatInput('{}: '.format(Tags['Header'][i])))
    print('\nData baru\n',tabulate([NewData],headers=Tags['Header']),'\n1. Simpan data\n2. Batalkan.')
    Save=OptInput(['1','2'],'Pilihan: ')
    if Save=='1':
        Data.append(NewData)
        Tags['PrimeKeys'].append(NewData[0])
        print('\nData berhasil disimpan.')
    else:
        print('\nData tidak tersimpan.')

#Update data menu
def UpdateMenu(Data,Tags):
    while True:
        print('\n1. Ubah data\n2. Kembali ke menu utama')
        Opt=OptInput(['1','2'],'Pilihan perintah: ')
        if Opt=='1':
            EditData(Data,Tags)
        elif Opt=='2':
            break

#Edit data
def EditData(Data,Tags):
    Key=IntInput('Masukkan ID peminjaman yang ingin diubah: ')
    if Key not in Tags['PrimeKeys']:
        print('Data tidak ditemukan.')
        return None
    k=Tags['PrimeKeys'].index(Key)
    print('\n',tabulate([Data[k]],headers=Tags['Header']),'\n1. Ubah data\n2. Batalkan.')
    Edit=OptInput(['1','2'],'Pilihan: ')
    if Edit=='2':
        print('Tidak ada perubahan.')
        return None
    print(''.join(['\n{}. {}.'.format(i,Tags['Header'][i]) for i in range(1,len(Tags['Header']))]))
    Field=OptInput([str(i) for i in range(1,len(Tags['Header']))],'Field yang ingin diubah: ')
    if Tags['Type'][int(Field)]==str:
        NewValue=input('{} baru: '.format(Tags['Header'][int(Field)])).capitalize()
    elif Tags['Type'][int(Field)]==int:
        NewValue=IntInput('{} baru: '.format(Tags['Header'][int(Field)]))
    elif Tags['Type'][int(Field)]==float:
        NewValue=FloatInput('{} baru: '.format(Tags['Header'][int(Field)]))
    print('\n1. Simpan data\n2. Batalkan')
    Save=OptInput(['1','2'],'Pilihan: ')
    if Save=='1':
        Data[k][int(Field)]=NewValue
        print('\nData berhasil diubah.')
    else:
        print('\nTidak ada perubahan.')

#Delete data menu
def DeleteMenu(Data,Tags):
    while True:
        print('\n1. Hapus data\n2. Kembali ke menu utama')
        Opt=OptInput(['1','2'],'Pilihan perintah: ')
        if Opt=='1':
            DelData(Data,Tags)
        elif Opt=='2':
            break

#Delete data
def DelData(Data,Tags):
    Key=IntInput('Masukkan ID peminjaman yang ingin dihapus: ')
    if Key not in Tags['PrimeKeys']:
        print('Data tidak ditemukan.')
        return None
    k=Tags['PrimeKeys'].index(Key)
    print('\n',tabulate([Data[k]],headers=Tags['Header']),'\n1. Hapus data\n2. Batalkan.')
    Delete=OptInput(['1','2'],'Pilihan: ')
    if Delete=='1':
        Data.pop(k)
        Tags['PrimeKeys'].pop(k)
        print('Data berhasil dihapus.')
    else:
        print('Tidak ada perubahan.')

#New Field Menu
def NewFieldMenu(Data,Tags):
    while True:
        print('\n1. Buat field baru\n2. Kembali ke menu utama')
        Opt=OptInput(['1','2'],'Pilihan perintah: ')
        if Opt=='1':
            AddField(Data,Tags)
        elif Opt=='2':
            break

#Add new field
def AddField(Data,Tags):
    NewField=input('Masukkan nama field baru: ').capitalize()
    if NewField in Tags['Header']:
        print('Field sudah ada.')
        return None
    print('\n1. Integer\n2. Float\n3. Lainnya (string)')
    NewType={'1':int,'2':float,'3':str}[OptInput(['1','2','3'],'Tipe data field: ')]
    print('\n1. Bisa diurut\n2. Tidak bisa diurut')
    NewSort={'1':True,'2':False}[OptInput(['1','2'],'Pilihan: ')]
    if len(Data)!=0:
        print('\n1. Lanjutkan ke pengisian data\n2. Batalkan')
        Fill=OptInput(['1','2'],'Pilihan: ')
        if Fill=='2':
            print('\nTidak ada perubahan.')
            return None
        ReadAll(Data,Tags)
        NewData=[]
        for i in range(len(Data)):
            if NewType==str:
                NewData.append(input('{} data {}: '.format(NewField,Data[i][0])).capitalize())
            elif NewType==int:
                NewData.append(IntInput('{} data {}: '.format(NewField,Data[i][0])))
            elif NewType==float:
                NewData.append(FloatInput('{} data {}: '.format(NewField,Data[i][0])))
    print('\n1. Tambahkan field (dan data) baru\n2. Batalkan')
    Save=OptInput(['1','2'],'Pilihan: ')
    if Save=='1':
        for i in range(len(Data)):
            Data[i].append(NewData[i])
        Tags['Header'].append(NewField)
        Tags['Type'].append(NewType)
        Tags['Sortable'].append(NewSort)
        print('\nField berhasil dibuat.')
    else:
        print('\nTidak ada perubahan.')

#Sort data menu
def SortMenu(Data,Tags):
    while True:
        print('\n1. Urutkan data\n2. Kembali ke menu utama')
        Opt=OptInput(['1','2'],'Pilihan perintah: ')
        if Opt=='1':
            SortData(Data,Tags)
        elif Opt=='2':
            break

#Sort data
def SortData(Data,Tags):
    if len(Data)==0:
        print('Data kosong.')
        return None
    ReadAll(Data,Tags)
    SortableFields=[Tags['Header'][i] for i in range(len(Tags['Header'])) if Tags['Sortable'][i]==True]
    print(''.join(['\n{}. {}.'.format(i+1,SortableFields[i]) for i in range(len(SortableFields))]))
    Field=OptInput([str(i+1) for i in range(len(SortableFields))],'Urutkan data berdasarkan field: ')
    Field=Tags['Header'].index(SortableFields[int(Field)-1])
    print('\n1. Menaik\n2. Menurun')
    Ord=OptInput(['1','2'],'Pilihan pengurutan: ')
    Ord={'1':False,'2':True}[Ord]
    Res=Data
    for i in range(len(Data)):
        Sorted=True
        for j in range(len(Data)-i-1):
            if (Res[j][Field]>Res[j+1][Field]) ^ Ord:
                Res[j],Res[j+1]=Res[j+1],Res[j]
                Sorted=False
        if Sorted:
            break
    print('\nHasil pengurutan\n',tabulate(Res,headers=Tags['Header']),'\n1. Simpan\n2. Batalkan')
    Save=OptInput(['1','2'],'Pilihan: ')
    if Save=='1':
        Data=Res
        Tags['PrimeKeys']=[x[0] for x in Data]
        print('\nData berhasil diurutkan.')
    else:
        print('\nTidak ada perubahan.')

MainMenuOpts={'1':ReadMenu,'2':CreateMenu,'3':UpdateMenu,'4':DeleteMenu,'5':NewFieldMenu,'6':SortMenu}
Dataset=[]
Datatag={'Header':['ID','Nama peminjam','Judul buku','Penulis buku','Tgl peminjaman','Tgl pengembalian'],'Type':[int,str,str,str,str,str],'Sortable':[True,True,True,True,False,False],'PrimeKeys':[x[0] for x in Dataset]}

MainMenu(Dataset,Datatag)

print('\nSelamat melanjutkan aktivitas.')