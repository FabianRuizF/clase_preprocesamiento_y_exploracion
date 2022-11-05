def clean_strings(row):
    if("," in row):
        return row.replace(",",".")
    if(len(re.findall("[A-Za-z]",row))!=0):
        return -444444
    if("" == row):
        return -999999
    if("." in row):
        return row
