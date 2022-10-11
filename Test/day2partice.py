t_shart=100
pant=200
belt=50
password=123
verification=12
shart=int(input('Enter shart prize:'))
if t_shart==shart:
    pants=int(input('Enter your pant prize:'))
    if pants==pant:
        belts=int(input('Enter your belt prize:'))
        if belts==belt:
            pass_word=int(input('Enter your password:'))
            if pass_word==password:
                veti_fication=int(input('Enter your verification code:'))
                if veti_fication==verification:
                    print('success ')
                else:
                    print('worng')
            else:
                print('password is worng')
        else:
            print('belt prize is worng')
    else:
        print('pant prize is worng')
else:
    print('prize is worng')