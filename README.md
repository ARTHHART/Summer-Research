# Summer-Research
Within this github there are 3 codes used for interperting the GiBUU output file

The first code is Outputfile.py and the second is AHT.java 
Outputfile.py works incredibly simply, it takes the inforamtion from the .lhe file that you will create a path too and reads the information in and reformats it. 

ex. "events = pylhe.read_lhe('EventOutput.Pert.00000001.lhe')"
As you can see the 'EventOut.Pert.00000001.lhe' file is the file I chose, change it as you see fit. This code will ony read in a .lhe so be aware. 

It will produce an output.txt file, which can be named in this line of code "output_file = open('output2.txt', 'w')" so change according to what you want. I have it as "outpu2.txt" 

The next code, AHT.java will read in the newly generated outputfile and read it, it will print out different graphs. Keep in mind this is based off the clas12 code so please look into that if you want a specific graph. 

You can read up on that here : https://clasweb.jlab.org/wiki/index.php/CLAS12_Software_-_Java_Analysis_Tools_Examples , Keep in mind this code is not the same as that code, this will only read the mentioned ouput file from the Outputfile.py, I modified the clas12 to being able to read in a .txt file. 

Within the code you will find a line "String filePath = "/home/hartel1/GiBUU/release/testRun/output2.txt";" this is where you will create your path to the file you wnt read in. 

There is another 3rd code new.py, this is for creating the test code and graph to see if the GiBUU works. 

The line of code where the information will be read in will be this "data = np.loadtxt("DileptonMass.dat")"
DileptonMass.dat should always be the file that is being read in 

If needed:
How to install the GiBUU, please reference : https://gibuu.hepforge.org/trac/wiki
first:
Create a new directory for GiBUU and change to that directory:
mkdir GiBUU; cd GiBUU

second:
wget --content-disposition https://gibuu.hepforge.org/downloads?f=release2023.tar.gz
tar -xzvf release2023.tar.gz

third:
wget --content-disposition https://gibuu.hepforge.org/downloads?f=buuinput2023.tar.gz
tar -xzvf buuinput2023.tar.gz

once thats all downloaded then type 
make 

once its all compiled then to run the GiBUU 
./GiBUU.x < my_setup.job/ 

after my_setup.job/ you will want to include a job card of what you want to run, all the jobcards are found within the directory testRun/jobCards
