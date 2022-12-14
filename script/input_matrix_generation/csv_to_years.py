import pandas as pd
filedata = pd.read_csv("./All_data.csv")
f = open("./junk.txt","w")
count = 0
len_data = filedata.shape[0]
#create template data to save the csv , and count postive or negative sample
years_data = {}
years_data_count = {}
#range csv form begin to the end
for i in range(len_data):
    if(i%100==0):
        print("------{:.2f}%------".format(100*(1.0*i)/len_data),end="\r")
    pair1 = filedata['Pair1'][i]
    pair2 = filedata['Pair2'][i]
    if(pair1 == 'A/REASSORTANT/NYMC-X-161B'):
        pair1 = '2005'
    if(pair2 == 'A/REASSORTANT/NYMC-X-161B'):
        pair2 = '2005'
    pair1 = int(pair1[-4:])
    pair2 = int(pair2[-4:])
    temp = max(pair1,pair2)
    if(not temp in years_data.keys()):
        years_data[temp] = pd.DataFrame(columns=['Pair1','Seq1','Pair2','Seq2','Length1','Length2','diff-seq','Class','Dij'])
        years_data[temp] = years_data[temp].append(filedata.iloc[i])
        years_data_count[temp] = [0,0]
        if(int(filedata['Class'][i])==0):
            years_data_count[temp][0] = years_data_count[temp][0] + 1
        if(int(filedata['Class'][i])==1):
            years_data_count[temp][1] = years_data_count[temp][1] + 1
    else:
        years_data[temp] = years_data[temp].append(filedata.iloc[i])
        if(int(filedata['Class'][i])==0):
            years_data_count[temp][0] = years_data_count[temp][0] + 1
        if(int(filedata['Class'][i])==1):
            years_data_count[temp][1] = years_data_count[temp][1] + 1
        
#save all template data
list_years = sorted(years_data.keys(),reverse=True)
ll = len(list_years)
for i in range(ll):  #   if i == ll-1 , data = all , we dont need it  ； data is i ,but name is i+1
    try:
        years_data[list_years[i]].to_csv("../csv/double/{}.csv".format(list_years[i]),index=False)
    except:
        print("error")
            
f.close()
print("Congratulation!We finish it!")
    
