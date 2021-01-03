"""
Copyright 2020 Dierk-Bent Piening

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import sys
from argparse import ArgumentParser
import pandas as pd
import json

def WelcomeMessage():
    print("excel2json v 1.0\n")
    print("©️ 2020 Dierk-Bent Piening\n")
    print("📧 d.b.piening@gmx.de\n")
    print("Software Programmed with ❤️ in Germany.\n")
    print("\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\n")

def ReadXLSX(filename, outputfiletxt, outputfilejson, sheetname):
    vdconverteddict = dict()
    vsrow = ""
    try:
        vdexceldic = pd.read_excel(filename, engine='openpyxl', index_col=0, sheet_name=sheetname).to_dict()
        print("File read: " + filename)
    except Exception as e:
        print("Error: Could not open XLSX file! ", str(e))
        exit()
    try:
        fobj_txt = open(outputfiletxt, "w")
        fobj_json = open(outputfilejson, "w")
    except Exception as e:
        print("Error: Could not open output file! ", str(e))
        exit()

    for p_id, p_info in vdexceldic.items():
        vdconverteddict[p_id] = list(p_info.values())
    for row in zip(*([key] + (value) for key, value in sorted(vdconverteddict.items()))):
        vsrow = vsrow + "\n" + str(row)
    try:
        fobj_txt.write(vsrow)
        fobj_json.write(json.dumps(str(vdconverteddict)))
    except Exception as e:
        print("Error: Could not write file! ", str(e))
    try:
        fobj_txt.flush()
        fobj_txt.close()
    except Exception as e:
        print("Error: Could not flush & close file! ", str(e))
        exit()
    try:
        fobj_json.flush()
        fobj_json.close()
    except Exception as e:
        print("Error: Could not flush & close file! ", str(e))
        exit()

    return json.dumps(str(vdconverteddict))

def convert2json(filename, outputfiletxt, outputfilejson, sheetname):
    return ReadXLSX(filename, outputfiletxt, outputfilejson, sheetname)

if __name__ == '__main__':
    WelcomeMessage()
    # Defining Arguments
    vapparser = ArgumentParser()
    vapparser.add_argument("--input", "-i", type=str, required=True)
    vapparser.add_argument("--outputjson", "-oj", type=str, required=True)
    vapparser.add_argument("--outputtxt", "-ot", type= str, required=True)
    vapparser.add_argument("--sheetname", "-sn", type= str, required=True)
    args = vapparser.parse_args()
    ReadXLSX(args.input, args.outputtxt, args.outputjson, args.sheetname)