'''
a=['cat','window','dog',20,30,10,40,50]
for x in a:
    print (x)
'''

'''
for i in range(1,10):
    print(i)
'''
'''
for i in range(10):
    if (i==5):
        break
    print(i)
'''

politicleParties=['AAP','Elephent','Hand','Rest']
electionYear=['2014','2009','2005','2001']
countryStatus=['worst','developing','developed']
corruptionStatus=['Max','Normal','Min']
for party in politicleParties:
    year=input('Enter your pass year:')
    if year in electionYear:
        if year=='2014':
            print('Aas winns!')
            print('country Status :' +corruptionStatus[2])
            print('corruption Starus :' +corruptionStatus[2])
            break
        elif year=='2009':
            print('Hand Won!')
            print('country Status :' + corruptionStatus[0])
            print('corruption Starus :' + corruptionStatus[0])
            continue
        elif year=='2005':
            print('Hand Won!')
            print('country Status :' + corruptionStatus[0])
            print('corruption Starus :' + corruptionStatus[0])
        elif year=='2001':
            print('Rest Won!!')
    else:
        print('Wrong year of election!')