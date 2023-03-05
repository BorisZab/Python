# проверка на создание одинокового контакта

from os import path

file_base = "base.txt"
file_edit = "edit.txt"
all_data = []
id = 0
all_data_mas = []
if not path.exists(file_base):
    with open(file_base,"w", encoding="utf-8") as _:
        pass

if not path.exists(file_edit):
    with open(file_edit,"w", encoding="utf-8") as _:
        pass

def read_records():
    global all_data, id

    with open(file_base) as f:
        all_data = [i.strip() for i in f ]
        if all_data : 
            id = int(all_data[-1][0])
        return all_data

def all_mas():
    global all_data, all_data_mas
    for i in all_data:
        i=0
        all_data_mas.append(all_data[i].split())
        i+=1
    return all_data_mas


def show_all():
       if not all_data:
           print("empty data")
       else:
        print(*all_data, sep="\n")

def add_record():
    global id
    array = ['surname', 'name','surname_2','phone_number']
    string = ''
    for i in array:
        string = string + input(f" enter {i} ")+ " " 
    id +=1
    # print(f'{id} {string}')2

    with open(file_base,"a", encoding="utf-8") as f:
        f.write(f'{id} {string}\n')
        pass
    
def delete_record():
    global id, all_data,file_base,file_edit
    del_rec = int(input("Chose ID record for delete:"))
    all_data = [k for k in all_data if k[0] != del_rec]

    print(all_data)

    pass

def edit_record():
    # read_records()
    all_mas()
    print(*all_data_mas)
    

def search_menu():
    
    global id, all_data, all_data_mas
    play = True
    
    while play:
        read_records()
        all_mas()
        temp=[]
        check =-1
        answer1 = input("Choose for search:\n"
                                "1. id\n"
                                "2. surname\n"
                                "3. name\n"
                                "4. surname_2\n"
                                "5. phone number\n"
                                "6. exit\n")
        match answer1:
            case "1":
                search = int(input("Write Id:"))-1
                if search >= 0 and search <= id:
                    print(all_data[search])
                else:
                    print("Id not found!")                    
            case "2":
                search = input("Write surname:")
                can = [k for k in all_data_mas if k[1] == search]
                print()
                print(can[2][0])
                
                # i= 0
                # for i in range(len(all_data_mas)):
                #     for j in range(len(all_data_mas[i])):
                #         if search == all_data_mas[i][1]:
                #             print(all_data[i]) 
                #             break            
                #         else:
                #             print("surname not found!")  
                #     i+=1
                # i = int(0)
                # for i in range(len(all_data_mas)):
                # while i <= 3:
                #         check = all_data_mas[i][1]
                #         temp.append(check)
                #         i=i+1
                    # if search in all_data:
                    #     print("1")
                    # else:
                    #     print("2")
                   
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                # i=0
                # search = input("Write phone number:")
                # for i in range(len(all_data_mas)):
                #     find = all_data_mas[i][4]
                #     # if find == search:
                #     #     print(all_data_mas[i])
                #     print(find)
                # i=i+1
                # else:
                #     print("Id not found!")  
                pass
            case "6":
                play = False
                
    # вывести весь список и попросить выбрать ид,
    # затем только поределенный констакт





def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Delete record\n"
                       "5. Edit record\n"
                       "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_record()
            case "3":
                search_menu()
            case "4":
                delete_record()
            case "5":
                edit_record()
            case "6":
                play = False
            case _:
                print("Try again!\n")
main_menu()
# print(read_records())
# read_records()

    


