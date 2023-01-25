#group titles, pictures and descriptions into a new report based on seed keywords. Add HTML <h3> tags for the titles within description.

#import libraries
import csv

insert_domain = "domain-name.com"
single_category = "Category"

#initialize lists
title_lst=[]
guid_lst=[]
price_lst=[]
domain_url=[]
image_url=[]
seed_lst=[]
description_lst=[]
date_lst=[]
group_seed_lst=[]
desc_lst=[]
excerpt_lst=[]
full_desc_lst=[]

# read input group seed keys
file_in = open("seed-keywords.csv", encoding="utf8")
with file_in as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            uTitle=''
            for x in row[0]:   #clean garbage characters from the titles
                if ord(x)<128:
                    uTitle= uTitle + x
            uTitle=uTitle.replace("?","")
            group_seed_lst.append(uTitle)            
file_in.close()


# read input group seed keys
file_in = open("data_to_be_grouped.csv", encoding="utf8")
with file_in as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            uTitle=''
            for x in row[0]:   #clean garbage characters
                if ord(x)<128:
                    uTitle= uTitle + x
            uTitle=uTitle.replace("?","")
            title_lst.append(uTitle)
            guid_lst.append(row[1]) 
            price_lst.append(row[2]) #convert to int from string in case of calculations
            #cat_lsd.append(row[3]) 
            #image_url.append(row[4])
            seed_lst.append(row[5])
            #description_lst.append(row[6])
            desc_lst.append("<div>"+"<h3>"+uTitle+"</h3>"+row[7]+"</div>")
            excerpt_lst.append(row[8])
            
file_in.close()

#Populate group description list

full_excerpt_lst=[]
for i in range(len(group_seed_lst)):
    temp_full_desc =""
    temp_full_excerpt =""
    for x in range(len(seed_lst)):
        if group_seed_lst[i]== seed_lst[x]:
            temp_full_desc = temp_full_desc + desc_lst[x]
            temp_full_excerpt = excerpt_lst[i]
    full_desc_lst.append(temp_full_desc)
    full_excerpt_lst.append(temp_full_excerpt)
    
# generate output report            
file_out = open("group_output_report.csv", "w")
for i in range(len(group_seed_lst)):
    file_out.write("Collection of " + group_seed_lst[i].title())
    file_out.write(",")
    file_out.write(full_desc_lst[i])
    file_out.write(",")
    file_out.write(single_category)
    file_out.write(",")
    file_out.write(full_excerpt_lst[i])
    file_out.write(",\"")
    file_out.write(group_seed_lst[i].lower().replace(" ",","))
    file_out.write("\"\n")

file_out.close()
#print(desc_lst[0])
print(group_seed_lst[0])
print(title_lst[0])
print(full_desc_lst[0])
            




