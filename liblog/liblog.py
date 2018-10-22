'''
@version: 2018-10-11

@author: Bodo Hugo Barwich
'''
from mock.mock import self



class LogMessage(object):
  '''
  This is a Class to manage accumulative Log and Error Strings and the numeric Error Code
  and return them as single String
  '''
   
  '''
  -----------------------------------------------------------------------------------------
  Attributes
  '''
  
      
  def __init__(self, logmessage = '', errormessage = '', errorcode = 0):
    '''
    A LogMessage Object can be instanciated providing and initial message
      
    :param string logmessage: A string Message that will be stored as 'LogMessage::report' string Attribute
    :param string errormessage: A string Message that will be stored as 'LogMessage::error' string Attribute  
    :param integer errormessage: A whole Number that will be stored single 'LogMessage::code' numeric Attribute  
    '''
    
    self._arr_rpt = []
    self._arr_err = []
    
    self._report = ''
    self._error_message = ''
    
    self._error_code = 0
    
    if logmessage != '' :
      self.setReport(logmessage)
      
    if errormessage != '' :
      self.setError(errormessage, errorcode)
    elif errorcode != 0 :
      self._error_code = errorcode
      
  
  def __del__(self):
    self._arr_log = None
    self._arr_err = None
  
  
   
  '''
  -----------------------------------------------------------------------------------------
  Administration Methods
  '''
  
      
  def addReport(self, message):
    '''
    Adds a Message to the Report String
    
    :param string message: A String that will be added to the self.report string attribute
    '''
    
    if message != '' :
      self._arr_rpt.append(message)
      self._report = ''
  
    
  def addError(self, message, code = 0):
    '''
    Adds an Error Message and an Error Code
    Errors are treated in an accumulative way that means that 
    the Error Code is only overwritten by an higher Error Code
    as described in `LogMessage.addErrorCode`
    
    :param string message: The Message to be added to the LogMessage.error Attribute
    :param integer code: The Error Code to be added
    :func:`addErrorCode`
    '''
    
    if message != '' :
      self._arr_err.append(message)
      self._error_message = ''
     
    self.addErrorCode(code) 
      
      
  def setReport(self, message = ''):
    self._arr_rpt = []
    self._report = ''
    
    if message != '' :
      self._arr_rpt.append(message)
    
    
  def setError(self, message = '', code = None):
    self._arr_err = []
    
    self._error_message = ''
    
    if code is not None :
      self._error_code = code
    
    if message != '' :
      self._arr_err.append(message)
      
      
  def addErrorCode(self, code):
    '''
    This will keep the Highest added Error Code in the Attribute LogMessage.code
    
    :param integer code: The Error Code to be added
    '''
    if code > self._error_code :
      self._error_code = code
      
      
  def setErrorCode(self, code = 0):
    '''
    This will overwrite the existing Error Code with the new Error Code
    
    :param integer code: The Error Code to overwrite the existing one
    '''
    self._error_code = code
    
      
  def clear(self):
    self._arr_rpt = []
    self._arr_err = []
    
    self._report = ''
    self._error_message = ''
    
    self._error_code = 0
    
  
  
  
  '''
  -----------------------------------------------------------------------------------------
  Consultation Methods
  '''

  
  def getReportArray(self):
    return self._arr_rpt
  
  
  def getErrorArray(self):
    '''
    :returns: The Error Messages as List of Strings
    :rtype list[string]
    '''
    return self._arr_err
    
      
  def getReportString(self):
    '''
    LogMessage.report Attribute which represents All Report Messages 
     
    :returns: All Report Messages as single String joined each one in a new Line
    :rtype list[string]
    '''
    if self._report == '' :
      self._report = '\n'.join(self._arr_rpt)
    
    return self._report
  
  
  def getErrorString(self):
    '''
    LogMessage.error Attribute which represents All Error Messages
    
    :returns: All Error Messages as single String joined each one in a new Line
    :rtype string
    '''
    if self._error_message == '' :
      self._error_message = '\n'.join(self._arr_err)
    
    return self._error_message
   
  
  def getErrorCode(self):
    '''
    LogMessage.code Attribute which represents the Highest Error Code
    
    :returns: The Highest recorded Error Code
    :rtype: integer
    '''
    return self._error_code
  
  
  report = property(getReportString, setReport)
  error = property(getErrorString, setError)
  code = property(getErrorCode, setErrorCode)
