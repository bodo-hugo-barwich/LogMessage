'''
@version: 2018-09-30

@author: Bodo Hugo Barwich
'''


class LogMessage(object):
  '''
  classdocs
  '''
  
  _report = ''
  _error_message = ''
  _error_code = 0


  def __init__(self, logmessage = None, errormessage = None, errorcode = None):
    '''
    Constructor
    '''
      
  def addLog(self, message):
    if not message == '' :
      self._report += message
  
    
  def addError(self, message, code = 0):
    if not message == '' :
      self._error_message += message
      
    if code > 0 and code > self._error_code :
      self._error_code = code
  
      
  def clear(self):
    self._report = ''
    self._error_message = ''
    self._error_code = 0
    
  