import os  
import re

def percentage(part, whole):
  return 100 * float(part)/float(whole)  
 
def parse(file): 
with open("../2016010805/mse01.kbu") as f:
    lines = f.readlines()
    found = 0
    found_jtree = 0
    j_counter = 0
    total = 0
    used = 0
    available = 0    
    for line in lines:
        #print line
        if re.match(r'^scripting@*.*> request pfe execute command "show jtree [0-9] memory" target fpc[0-9] \| no-more ', line):
            #print line
            fpc = re.search("fpc*[0-9]", line)
            fpc_no = re.search("\d+", fpc.group(0))
            print fpc_no.group(0)
            #print "found"
            found = 1        
        if (found == 1 and re.match(r'^GOT: Jtree memory segment [0-9] \(Context: *.*\)', line)):
            found_jtree = 1
            j_counter = 0
            total = 0
            used = 0
            available = 0
        if found_jtree == 1:
            print "hit ---------"
            if j_counter == 3:
                total = int(re.search(r'\d+' , line).group(0))
                print line
            if j_counter == 4:
                used = int(re.search(r'\d+' , line).group(0))
            if j_counter == 5:
                available = int(re.search(r'\d+' , line) .group(0))
                found_jtree = 0                             
                print "Total = %s, Used = %s, Available = %s , Usage percentage = %s \n" %  (total, used , available, percentage(used, total))
        j_counter += 1
 
def main():
        for fn in os.listdir('../2016010805'):
        print fn
        name = fn
        full_path = "../2016010805/" + fn

if __name__ == "__main__":
    main()
       
