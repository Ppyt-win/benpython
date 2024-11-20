# # # print('f hello {name_of_students:}')
# # # name_of_students = input(('enter your name:'))

# # # pass_mark = int(input('enter your score:'))
# # # if pass_mark > 50 or pass_mark == 50:
#     print(f'hi {name_of_students} you passed')
# # a, b = 10,20
# # if 'foo' in ['foo','bar','wat']:
# #     print('innit')
# #     if a > b:
# #         print('true')
# #     else:
# #         print('false')
    
# #     print('done')

# #     if a < b:
# #         print(ce*20/100
# print('you are given $160 as discount')
# if Amount <100:
#     print('no discount')'yes')
    
# #     print('another one')
# # print('the end')



Amount = int(input('Enter Amount:'))
original_price =700
Amount_to_pay =800
discount =Amount*20/100
Tax = discount*8/100
if Amount < 100:
    print('Hello,customer! You have no discount')
elif Amount ==100 or Amount <=500:
    print(f'Hello, customer! You have a 10% discount of $ {discount} and a 5% VAT of ${Tax}. You are to pay ${Amount-discount+Tax} Thanks.')
elif Amount >500:
    print(f'Hello, customer! You have a 20% discount of ${discount} and an 8% VAT of ${Tax}. You are to pay ${Amount-discount+Tax}Thanks')

    

