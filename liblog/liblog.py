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


  def __setattr__(self, name, value):
    if name == 'report' :
      self.setLog(value)
    elif name == 'error' :
      self.setError(value)
    elif name == 'code' :
      self._error_code = value
    else :
      raise AttributeError('Attribute {} : Attribute does not exist'.format(name))
      
      
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
  
  
  def getReportArray(self):
    return self._arr_log
  
  
  def getErrorArray(self):
    return self._arr_err
    
      
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
  
  
  def __getattribute__(self, name):
    if name == 'report' :
      return self.getReportString()
    elif name == 'error' :
      return self.getErrorString()
    elif name == 'code' :
      return self.getErrorCode()
    else :
      raise AttributeError('Attribute {} : Attribute does not exist'.format(name))
