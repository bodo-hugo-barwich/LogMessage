'''
This Module provides the `LogMessage` Class which implements an accumulative Log 
and Error strings management.

:version: 2018-10-22

:author: Bodo Hugo Barwich
'''
__docformat__ = "restructuredtext en"


from mock.mock import self



class LogMessage(object):
  '''
  This is a Class to manage accumulative Log and Error strings and the numeric Error Code
  and return them as single String
  
  It offers Methods to progressively add Messages to the Log or Error Registry
  
  The Error Code is accumulative since it keeps only the Highest Value.
  
  It publishes the complete merged Message as Properties
    
  :undocumented: LogMessage._arr_rpt
  :undocumented: LogMessage._arr_err
  
  :see: `LogMessage.report`
  :see: `LogMessage.error`
  :see: `LogMessage.code`
  '''

  #-----------------------------------------------------------------------------------------
  #Constructors

      
  def __init__(self, logmessage = '', errormessage = '', errorcode = 0):
    '''
    A LogMessage Object can be instanciated providing initial Report Message, 
    Error Message and Error Code
      
    :param logmessage: A string Message that will be stored as `LogMessage.report` string Property
    :type logmessage: string
    :param errormessage: A string Message that will be stored as `LogMessage.error` string Property
    :type errormessage: string  
    :param errorcode: A whole Number that will be stored single `LogMessage.code` numeric Property
    :type errorcode: integer
    
    :see: `LogMessage.report`
    :see: `LogMessage.error`
    :see: `LogMessage.code`
    '''
    
    self._arr_rpt = []
    self._arr_err = []
    
    self._report = None
    self._error_message = None
    
    self._error_code = 0
    
    if logmessage != '' :
      self.setReport(logmessage)
      
    if errormessage != '' :
      self.setError(errormessage, errorcode)
    elif errorcode != 0 :
      self.setErrorCode(errorcode)
      
  
  def __del__(self):
    '''
    On Destruction the Lists of strings will be freed
    '''
    self._arr_log = None
    self._arr_err = None
  
  
   
  #-----------------------------------------------------------------------------------------
  #Administration Methods


  def addReport(self, message):
    '''
    Adds a Message to the Report String
    
    :param message: A String that will be added to the LogMessage.report string Property
    :type message: string
    :see: `LogMessage.report`
    '''
    
    if message != '' :
      self._arr_rpt.append(message)
      self._report = None
  
    
  def addError(self, message, code = 0):
    '''
    Adds an Error Message and an Error Code.
    Errors are treated in an accumulative way that means that 
    the Error Code is only overwritten by an higher Error Code
    as described in `LogMessage.addErrorCode`
    
    :param message: The Message to be added to the `LogMessage.error` Property
    :type message: string
    :param code: The Error Code to be added
    :type code: integer
    :see: `LogMessage.addErrorCode`
    '''
    
    if message != '' :
      self._arr_err.append(message)
      self._error_message = None
     
    self.addErrorCode(code) 
      
      
  def setReport(self, message = ''):
    '''
    This Method sets by Replacement the `LogMessage.report` string 
    
    :param message: The Message string thet replaces the former\
      Report Message string
    :type message: string
    '''
    self._arr_rpt = []
    self._report = ''
    
    if message != '' :
      self._arr_rpt.append(message)
    
    
  def setError(self, message = '', code = None):
    '''
    This Method sets by Replacement the `LogMessage.error` string and 
    sets and replaces the `LogMessage.code` Error Code
    
    :param message: The Message string that replaces former
      the former Error Message String
    :type message: string
    :param code: The Error Code that replaces the former
      Error Code
    :type code: integer
    '''
    self._arr_err = []
    self._error_message = None
    
    if message != '' :
      self._arr_err.append(message)
      
    if code is not None :
      self._error_code = code
    
      
  def addErrorCode(self, code):
    '''
    This will keep the Highest added Error Code in the Attribute LogMessage.code
    
    :param code: The Error Code to be added
    :type code: integer 
    '''
    if code > self._error_code :
      self._error_code = code
      
      
  def setErrorCode(self, code = 0):
    '''
    This will overwrite the existing Error Code with the new Error Code
    
    :param code: The Error Code to overwrite the existing one
    :type code: integer
    '''
    self._error_code = code
    
      
  def clear(self):
    '''
    Resets the `LogMessage.report`, `LogMessage.error` and `LogMessage.code` Property
    It empties the Lists and resets the Output Buffer.
    '''
    self._arr_rpt = []
    self._arr_err = []
    
    self._report = None
    self._error_message = None
    
    self._error_code = 0
    
  
  
  
  
  #-----------------------------------------------------------------------------------------
  #Consultation Methods

  
  def getReportArray(self):
    '''
    :returns: The Report Messages as List of Strings
    :rtype: list[string]
    '''
    return self._arr_rpt
  
  
  def getErrorArray(self):
    '''
    :returns: The Error Messages as List of Strings
    :rtype: list[string]
    '''
    return self._arr_err
    
      
  def getReportString(self):
    '''
    LogMessage.report Property which represents All Report Messages 
     
    :returns: All Report Messages as single String joined each Message in a new Line
    :rtype: string
    '''
    if self._report is None :
      self._report = '\n'.join(self._arr_rpt)
    
    return self._report
  
  
  def getErrorString(self):
    '''
    LogMessage.error Property which represents All Error Messages
    
    :returns: All Error Messages as single String joined each Massage in a new Line
    :rtype: string
    '''
    if self._error_message is None :
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
