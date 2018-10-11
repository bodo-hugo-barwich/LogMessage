'''
Tests to verify the LogMessage Class Functionality

@version: 2018-10-08

@author: Bodo Hugo Barwich
'''
import sys
import unittest

sys.path.append("../liblog")

from liblog import LogMessage


class TestLogMessage(unittest.TestCase):

  _arr_test_log = ["first log text 0", "log text 1", "log text 2", "log text 3"]
  _arr_test_error = ["first error text 0", "error text 1", "error text 2", "error text 3"]
  _arr_test_codes = [0, 1, 2, 3]

  def setUp(self):
    pass


  def tearDown(self):
    pass


  def test_Constructor(self):
    print("{} - go ...\n".format(sys._getframe().f_code.co_name))
    
    logmsg = LogMessage()    
    
    print("testConstructor - Report: '{}'".format(logmsg.getReportString()))
    print("testConstructor - Error: '{}'".format(logmsg.getErrorString()))
    print("testConstructor - Code: '{}'".format(logmsg.getErrorCode()))
    
    self.assertEqual(logmsg.getReportString()\
    , "", "Report is not empty.\n")
    self.assertEqual(logmsg.getErrorString()\
    , "", "Error is not empty.\n")
    self.assertEqual(logmsg.getErrorCode()\
    , 0, "Code is not '0'.\n")
  
  
  def test_AddReport(self):
    print("{} - go ...\n".format(sys._getframe().f_code.co_name))
    
    logmsg = LogMessage(self._arr_test_log[0])
    
    logmsg.addReport(self._arr_test_log[1])
    logmsg.addReport(self._arr_test_log[2])
    logmsg.addReport(self._arr_test_log[3])
        
    print("testAddReport - Report: '{}'".format(logmsg.getReportString()))
    
    self.assertEqual(logmsg.getReportString()\
    , "\n".join(self._arr_test_log), "Multi Line Report Message uncomplete.\n")
    
    logmsg.clear()
    
    self.assertEqual(logmsg.getReportString()\
    , "", "Report not cleared.\n")
        
    print("testAddReport - Report: '{}'".format(logmsg.getReportString()))


  def test_SetReport(self):
    print("{} - go ...\n".format(sys._getframe().f_code.co_name))
    
    logmsg = LogMessage(self._arr_test_log[0])
    
    logmsg.setReport(self._arr_test_log[1])
    
    print("testAddReport - Report: '{}'".format(logmsg.getReportString()))
    
    self.assertEqual(logmsg.getReportString()\
    , self._arr_test_log[1], "Set Report Message does not match.\n")


  def test_AddError(self):
    print("{} - go ...\n".format(sys._getframe().f_code.co_name))

    logmsg = LogMessage("", self._arr_test_error[0])
    
    logmsg.addError(self._arr_test_error[1], self._arr_test_codes[0])
    logmsg.addError(self._arr_test_error[2], self._arr_test_codes[1])
    logmsg.addError(self._arr_test_error[3])
    
    print("testAddError - Error: '{}'".format(logmsg.getErrorString()))
    print("testAddError - Code: '{}'".format(logmsg.getErrorCode()))
    
    self.assertEqual(logmsg.getErrorString()\
    , "\n".join(self._arr_test_error), "Multi Line Error Message uncomplete.\n")
    
    self.assertEqual(logmsg.getErrorCode()\
    , self._arr_test_codes[1], "Error Code does not match.\n")


  def test_SetError(self):
    print("{} - go ...\n".format(sys._getframe().f_code.co_name))

    logmsg = LogMessage("", self._arr_test_error[0])
    
    logmsg.setError(self._arr_test_error[1], self._arr_test_codes[1])

    self.assertEqual(logmsg.getErrorString()\
    , self._arr_test_error[1], "Multi Line Error Message uncomplete.\n")
    
    self.assertEqual(logmsg.getErrorCode()\
    , self._arr_test_codes[1], "Error Code does not match.\n")


  def test_Clear(self):
    print("{} - go ...\n".format(sys._getframe().f_code.co_name))
    
    logmsg = LogMessage(self._arr_test_log[0])
    
    logmsg.addReport(self._arr_test_log[1])

    print("test_Clear - Report 1: '{}'".format(logmsg.getReportString()))
    
    logmsg.clear()
    
    self.assertEqual(logmsg.getReportString()\
    , "", "Report not cleared.\n")
        
    print("test_Clear - Report 2: '{}'".format(logmsg.getReportString()))
    
    logmsg.addReport(self._arr_test_log[2])

    print("test_Clear - Report 3: '{}'".format(logmsg.getReportString()))
    
    self.assertEqual(logmsg.getReportString()\
    , self._arr_test_log[2], "Report not correctly cleared.\n")

    


if __name__ == "__main__":
  print("tests starting ...\n")
  #import sys;sys.argv = ['', 'Test.testConstructor']
  unittest.main()
  
  print("tests done.\n")
  
  
  