phone_book = {'vache':'+37498340159', 'gexam':'+37498642133'}
phone = input('phone ')
for key,item in phone_book.items() :
    if item == phone:
        print(key)