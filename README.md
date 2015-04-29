# EPM Outline Comparison
This utlity is used to analize xml outline files. These files are
generally produced via the 
[EPMA File Generator](http://www.oracle.com/webfolder/technetwork/tutorials/obe/hyp/HFM11.1.2_MExtract/MetadataExtract-Files.htm)
or the Essbase 
[MaxL Export Outline](https://docs.oracle.com/cd/E17236_01/epm.1112/esb_tech_ref/frameset.htm?maxl_expotl.html)
utlity. When used with a single file the utility will print out
a sorted list of all the members of the outline and what dimension 
they exist in. When both file parameters are filled the utility will 
print [diff](http://en.wikipedia.org/wiki/Diff_utility) style comparison.

## Requirements
* [Python](https://www.python.org/)/[Jython](http://www.jython.org/)
* [lxml](http://lxml.de/)

## Usage
python outline_compare.py [xml file]
python outline_compare.py [xml file] [xml file]

### Example 1:
	kkikta@localhost:~/sgames$ python outline_compare.py Outline.xml | more
	 Account|A1000
	 Account|A1500
	 Account|Allocations
	 Account|Amortization
	 Account|Amortization New Equipment
	 Account|Amortization_Intangible
	 Account|Annual Average Cash Flow
	 ...

### Example 2:
	kkikta@localhost:~/sgames$ python outline_compare.py Outline1.xml Outline2.xml
	>  Account|Finished Goods
	>  Account|Maintenance Rev
	>  Account|Net Change
	>  Profit Center|PC_123012
	>  Profit Center|PC_123013
	<  Account|A95000
	<  Account|A95005
	<  Profit Center|PC_987000
	<  Profit Center|PC_987002
	<  Year|FY12
