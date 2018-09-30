'''
@version: 2018-09-30

@author: Bodo Hugo Barwich
'''



class LogMessage(object):
  '''
  classdocs
  '''
   
  '''
  -----------------------------------------------------------------------------------------
  Attributes
  '''
  
      
  _arr_log = []
  _arr_err = []
  
  _report = ''
  _error_message = ''
  
  _error_code = 0


  def __init__(self, logmessage = '', errormessage = '', errorcode = 0):
    '''
    Constructor
    '''    
    
    if logmessage != '' :
      self.addLog(logmessage)
      
    if errormessage != '' :
      self.addError(errormessage, errorcode)
    else :
      self._error_code = errorcode
      
  
  def __del__(self):
    self._arr_log = None
    self._arr_err = None
  
  
   
  '''
  -----------------------------------------------------------------------------------------
  Administration Methods
  '''
  
      
  def addLog(self, message):
    '''
    Adds a Message to the Report String
    '''
    
    if message != '' :
      self._arr_log.append(message)
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
      
      
  def setLog(self, message = ''):
    self._arr_log = []
    self._report = ''
    
    if message != '' :
      self._arr_err.append(message)
    
    
  def setError(self, message = '', code = 0):
    self._arr_err = []
    
    self._error_message = ''
    
    self._error_code = code
    
    if message != '' :
      self._arr_err.append(message)

      
  def clear(self):
    self._arr_log = []
    self._arr_err = []
    
    self._report = ''
    self._error_message = ''
    
    self._error_code = 0
    
  
  
  
  '''
  -----------------------------------------------------------------------------------------
  Consultation Methods
  '''
  
      
  def getReportString(self):
    if self._report == '' :
      self._report = '\n'.join(self._arr_log)
    
    return self._report
  
  
  def getErrorString(self):
    if self._error_message == '' :
      self._error_message = '\n'.join(self._arr_err)
    
    return self._error_message
   
  
  def getErrorCode(self):
    return self._error_code
  
