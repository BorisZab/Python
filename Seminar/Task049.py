# проверка на создание одинокового контакта

from os import path

file_base = "base.txt"

all_data = []
id = 0
all_data_mas = []
if not path.exists(file_base):
    with open(file_base,"w", encoding="utf-8") as _:
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
    
    for i in range(len(all_data)):
        
        s = list(map(str, all_data[i].split()))
        all_data_mas.append(s)
        
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
    
    with open(file_base,"a", encoding="utf-8") as f:
        f.write(f'{id} {string}\n')
        pass
    
def delete_record():
    
    global  all_data
    show_all()
    del_rec = input("Chose ID record for delete:")
    temp = [item[0] for item in all_data]
    if del_rec  in temp:
        print(f'Successful deletion {all_data[int(del_rec)]}')
        all_data = [k for k in all_data if k[0] != del_rec]
        with open(file_base,"w", encoding="utf-8") as f:
         for line in all_data:
                f.write(line)
                f.write('\n')
    else:
        print("Not correct ID !\n ")
    
   

    

def edit_record():
   
    global all_data,all_data_mas
    show_all()
    all_mas()
    string = ''
    edit_id = input("Chose ID record for edit:")
    temp = [item[0] for item in all_data]
    print(temp)
    if edit_id in temp:
        play = True
        print(all_data[temp.index(edit_id)])
        while play:
            read_records()
            answer = input("Phone book:\n"
                       "1. Edit surname\n"
                       "2. Edit name\n"
                       "3. Edit surname_2\n"
                       "4. Edit phone_number\n"
                       "0. Exit\n")
                       
            match answer:
                case "1":
                    edit = input("Write new surname:")
                    all_data_mas[temp.index(edit_id)][1]= edit
                    for i in range(len(all_data_mas[temp.index(edit_id)])):
                        string = string + all_data_mas[temp.index(edit_id)][i] + " "
                    for i in range(len(all_data)):
                        if all_data[temp.index(edit_id)] == all_data[i]:
                            all_data[temp.index(edit_id)] = string
                    with open(file_base,"w", encoding="utf-8") as f:
                        for line in all_data:
                            f.write(line)
                            f.write('\n')
                    print(f'Successful deletion {all_data[temp.index(edit_id)]}')

                case "2":
                    edit = input("Write new name:")
                    all_data_mas[temp.index(edit_id)][2]= edit
                    for i in range(len(all_data_mas[temp.index(edit_id)])):
                        string = string + all_data_mas[temp.index(edit_id)][i] + " "
                    for i in range(len(all_data)):
                        if all_data[temp.index(edit_id)] == all_data[i]:
                            all_data[temp.index(edit_id)] = string
                    with open(file_base,"w", encoding="utf-8") as f:
                        for line in all_data:
                            f.write(line)
                            f.write('\n')
                    print(f'Successful deletion {all_data[temp.index(edit_id)]}')
                case "3":
                    edit = input("Write new surname_2:")
                    all_data_mas[temp.index(edit_id)][3]= edit
                    for i in range(len(all_data_mas[temp.index(edit_id)])):
                        string = string + all_data_mas[temp.index(edit_id)][i] + " "
                    for i in range(len(all_data)):
                        if all_data[temp.index(edit_id)] == all_data[i]:
                            all_data[temp.index(edit_id)] = string
                    with open(file_base,"w", encoding="utf-8") as f:
                        for line in all_data:
                            f.write(line)
                            f.write('\n')
                    print(f'Successful deletion {all_data[temp.index(edit_id)]}')
                case "4":
                    edit = input("Write new phone_number:")
                    all_data_mas[temp.index(edit_id)][4]= edit
                    for i in range(len(all_data_mas[temp.index(edit_id)])):
                        string = string + all_data_mas[temp.index(edit_id)][i] + " "
                    for i in range(len(all_data)):
                        if all_data[temp.index(edit_id)] == all_data[i]:
                            all_data[temp.index(edit_id)] = string
                    with open(file_base,"w", encoding="utf-8") as f:
                        for line in all_data:
                            f.write(line)
                            f.write('\n')
                    print(f'Successful deletion {all_data[temp.index(edit_id)]}')
                case "0":
                    play= False
    else:
        print("Not correct ID !\n ")
   
    
    

def search_menu():
    
    global id, all_data, all_data_mas
    play = True
   
    while play:
        read_records()
        all_mas()
        temp=[]
     
        answer1 = input("Choose for search:\n"
                                "1. id\n"
                                "2. surname\n"
                                "3. name\n"
                                "4. surname_2\n"
                                "5. phone number\n"
                                "0. exit\n")
        match answer1:
            case "1":
                search = input("Write Id:")
                temp = [item[0] for item in all_data]
                if search in temp:
                    print(all_data[int(search)])
                else:
                    print("Id not found!")                    
            case "2":
                search = input("Write surname:")
                temp = [item[1] for item in all_data_mas]
                if search not in temp:
                    print("Surname not found!\n")
                else:
                    print(all_data[temp.index(search)])
            case "3":
                search = input("Write surname:")
                temp = [item[2] for item in all_data_mas]
                if search not in temp:
                    print("Name not found!\n")
                else:
                    print(all_data[temp.index(search)])
                pass
            case "4":
                search = input("Write surname:")
                temp = [item[3] for item in all_data_mas]
                if search not in temp:
                    print("Surname_2 not found!\n")
                else:
                    print(all_data[temp.index(search)])
                pass
            case "5":
                search = input("Write surname:")
                temp = [item[4] for item in all_data_mas]
                if search not in temp:
                    print("Phone number not found!\n")
                else:
                    print(all_data[temp.index(search)])
                pass 
            case "0":
                play = False
               

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
                       "0. Exit\n")
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
            case "0":
                play = False
            case _:
                print("Try again!\n")
main_menu()

    


