import os

# p = 'C:\\Users\\Corrupted\\Desktop\\test_sem'
p = 'G:/Download/Compressed/rico_dataset_v0.1_semantic_annotations/semantic_annotations'
# cc = open('data.csv', 'w')
cc2 = open('data2_all.csv', 'w')
cc2.write('name,component\n')
# llog=open('log.txt','w')
start=1
for i in os.listdir(p):
    if i.endswith('.json'):
        component = 0
        component_list=list()
        try:
            json_file = open(os.path.join(p, i))
            for j in json_file:
                if j.find('componentLabel') != -1:
                    label=j.split(':')[1].replace('"','')
                    component_list.append(label)
                    component += 1                    
            output=i+','+str(component)
            cc2.write(output+'\n')
            # for k in component_list:
            #     output+=','+k.strip()+','
            # output+='\n'
            # cc.writelines(output)
            os.system('cls')
            print(start)
            start+=1
        except UnicodeDecodeError:
            # llog.write(i+' problem'+'\n')
            print(i+' problem')
        

