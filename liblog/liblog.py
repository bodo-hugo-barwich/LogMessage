'''
@version: 2018-10-06

@author: Bodo Hugo Barwich
'''



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
    
    Parameters
    ----------
    logmessage : string
      A string Message that will be stored as 'log' string Attribute
    errormessage : string
      A string Message that will be stored as 'error' string Attribute
    errorcode : integer
      A whole Number that will be stored single 'code' numeric Attribute
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
    '''
    
    if message != '' :
      self._arr_rpt.append(message)
      self._report = ''
  
    
  def addError(self, message, code = 0):
    '''
    Adds an Error Message and an Error Code
    '''
    
    if message != '' :
      self._arr_err.append(message)
      self._error_message = ''
      
    if code > 0 and code > self._error_code :
      self._error_code = code
      
      
  def setReport(self, message = ''):
    self._arr_rpt = []
    self._report = ''
    
    if message != '' :
      self._arr_rpt.append(message)
    
    
  def setError(self, message = '', code = None):
    self._arr_err = []
    
    self._error_message = ''
    
    if code is None :
      self._error_code = code
    
    if message != '' :
      self._arr_err.append(message)
      
      
  def setErrorCode(self, code = 0):
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
    return self._arr_err
    
      
  def getReportString(self):
    if self._report == '' :
      self._report = '\n'.join(self._arr_rpt)
    
    return self._report
  
  
  def getErrorString(self):
    if self._error_message == '' :
      self._error_message = '\n'.join(self._arr_err)
    
    return self._error_message
   
  
  def getErrorCode(self):
    return self._error_code
  
  
  report = property(getReportString, setReport)
  error = property(getErrorString, setError)
  code = property(getErrorCode, setErrorCode)
