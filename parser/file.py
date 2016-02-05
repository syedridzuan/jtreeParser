import os  
import re
import pprint
#from mydb import connect
from ConfigParser import SafeConfigParser

def percentage(part, whole):
  return round(100 * float(part)/float(whole),2) 
  
def dbcommit(host, result):
    print "commit"
    

 
def parse(file): 
    with open(file) as f:
        jtree_arr = []
        lines = f.readlines()
        found = 0
        found_jtree = 0
        j_counter = 0
        total = 0
        used = 0
        available = 0
        jtree_no = 0       
        for line in lines:
            #print line
            if re.match(r'^scripting@*.*> request pfe execute command "show jtree [0-9] memory" target fpc[0-9] \| no-more ', line):
                #print line
                fpc = re.search("fpc*[0-9]", line)
                fpc_no = re.search("\d+", fpc.group(0)).group(0)
                #print fpc_no.group(0)
                #print "found"
                found = 1    
                jtree_no = None                
            if (found == 1 and re.match(r'^GOT: Jtree memory segment [0-9] \(Context: *.*\)', line)):
                segment = re.search(r'\d+', line).group(0)
                found_jtree = 1
                j_counter = 0
                total = 0
                used = 0
                available = 0
       
            if (found == 1 and re.match(r'^SENT\: Ukern command\: show jtree [0-9] memory' , line)):
                jtree_no = re.search(r'\d+', line).group(0)        
                print jtree_no                
            if found_jtree == 1:
                if j_counter == 3:
                    total = int(re.search(r'\d+' , line).group(0))
                    #print line
                if j_counter == 4:
                    used = int(re.search(r'\d+' , line).group(0))
                if j_counter == 5:
                    available = int(re.search(r'\d+' , line) .group(0))
                    found_jtree = 0                             
                    #print "Total = %s, Used = %s, Available = %s , Usage percentage = %s \n" %  (total, used , available, percentage(used, total))
                    jtree_arr.append([fpc_no, jtree_no, segment, used , available, percentage(used, total)])
            j_counter += 1
    return jtree_arr
 
def main():
    config = SafeConfigParser()
    config.read('config.ini')
    folder = config.get('jtree', 'folder')
    ins_sql = config.get('jtree', 'sql')
    for fn in os.listdir(folder):
        print fn
        name = fn
        full_path = folder + fn
        result = parse(full_path)
        pprint.pprint(result)
        #cnx_router = connect(1)
        #cursor_router = cnx_router.cursor()
        query = ("")
        for item in result:
            sql = ins_sql
            print sql            

if __name__ == "__main__":
    main()
       
