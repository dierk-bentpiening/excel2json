# excel2json
## Convert XLSX to json and txt.  
## Python Extension and Standalone Application

### Where can i download a Release:
Builded Binary versions for standalone usage and as python extension are available under the Release section.  
I Provide versions for:  

Windows x86_64  
Windows ARM64  
Linux x86_64  
Linux ARM64  
MacOS x86_64 (Future)  
MacOS ARM64 (Future)  
(Linux x86_64 versions should also work on MacOS)


### Build it by yourself:

**To Build Python extension:**  

Make sure that python3, python3-pip, python3-dev and cython3 is installed on your system.  
To do that on Debian / Ubuntu Linux type the following in to your terminal: 
 
`sudo apt install python3 python3-pip python3-dev cython`  

Now you should be able to build excel2json with the following commands:  

`python3 -m pip install -r requirements.txt`  

`python3 BuildExcel2jsonExtension.py build_ext --inplace`  

**To Build Standalone Application:**  

Make sure that python3, python3-pip, python3-dev and cython3 is installed on your system.  
To do that on Debian / Ubuntu Linux type the following in to your terminal:  

`sudo apt install python3 python3-pip python3-dev cython`  
  
Change Python version in BuildStandAlone.sh to the mathing version of Python3 installed on your system.  
 
`chmod -x BuildStandAlone.sh`  
`./BuildStandAlone.sh`  

### How to use it ?  

**Usage Extension:**
  
`from excel2json import convert2json`  
`resultjson = convert2json("XLSX/test3.xlsx", "test.txt", "test.json", "Tabelle1")`

**Usage Standalone:**    
  
`usage: excel2json.run [-h] --input INPUT --outputjson OUTPUTJSON --outputtxt OUTPUTTXT --sheetname SHEETNAME`  
  
***Usage in Batch mode:**  
  
Runs Batch Converting on all xlsx Files in the folder XLSX/ with the first Sheet of the file.  
  
`./excel2json.run -bp XLSX/`  

Runs Batch Converting on all xlsx Files in the folder XLSX/ with the sheet with the name "Sheet1".  
  
`./excel2json.run -bp XLSX/ -sn Sheet1`  
  


  
  
  

  
### Future ?
In the Future more options to customize JSON will be available also a Option to select a range of Columns and Rows.  
In the Future also an option for converting Excel to a sqlite DB / Create Script for PostgreeSQL will be available.  



**Software Programmed with ❤️ in Germany.**  
**We ❤️ open source!**  


