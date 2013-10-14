G2SageMath
==========

### Integrating Google spreadsheets to Sage math library

	======================   Author  ============================
	|															|
	|	M.P. Tharindu Rusira Kumara (tharindurusira@gmail.com) 	|
	|	  Department of Computer Science and Engineering        | 
	|	  University of Moratuwa                                | 
	|	  Sri Lanka                                             | 
	|															|
	=============================================================
 
 
 Version 1.0 release : 14-Oct-2013
 
 More details: 
 http://tharindu-rusira.blogspot.com/2013/08/g2sagemath.html
 
## G2SageMath requirements

	* Linux based OS
	* Python 2.7 

## Running G2SageMath

* Download G2SageMath
* Extract it to any directory (say ~/)
* Execute the following line
	`python ~/G2SageMath/src/run.py`
	
* Follow the instructions on the terminal
* A successful G2SageMath run will load your csv file to sage
* This data file will be loaded into sage with identifier `file`
* Call 'file' in the newly opened sage terminal 
	`sage: file`

  
## Running the test-suite


1. Run with Eclipse (recommended)
  1. Install PyUnit for Eclipse
  2. Import G2SageMath as an Eclipse project
  3. Run `Test_g2sagemathlogin.py` and `Test_g2sagemathdata.py`
	

2. Run with the Linux terminal
  1. add `./src` directory to the system path before running the test cases
	
  2. Then run the test module
		
		`python Test_g2sagemathlogin`
		`python Test_g2sagemathdata`


## Installation


G2SageMath is a portable collection of Python scripts that you do not have to install anything.

A part of the the google-api-python-client library and other dependencies are included in this application, but these libraries have not been installed on your system. That means that this program will run from within the unzipped directory, but from nowhere else.  

An ambitious user may install the whole gdata-python-client library, but this is not required to run G2SageMath 

The easiest way to install the client library into your system is by running easy_install:

  `easy_install --upgrade google-api-python-client`

You might need to add a `sudo` to the beginning of that command depending on your platform.
If you don't have `easy_install` you can get it by installing the `setuptools` package.

 

