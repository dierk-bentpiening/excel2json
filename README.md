# excel2json
### Convert XLSX to json and txt.  
### Python Extension and Standalone Application

**To Build Python extension run:**  
`python3 BuildExcel2jsonExtension.py build_ext --inplace`

**To Build Standalone Application:**  
`chmod -x BuildStandAlone.sh
./BuildStandAlone.sh`

**Usage Extension:**  
`from excel2json import convert2json
resultjson = convert2json("XLSX/test3.xlsx", "test.txt", "test.json")`

**Usage Standalone:**  
usage: excel2json.run [-h] --input INPUT --outputjson OUTPUTJSON --outputtxt OUTPUTTXT


