############
Test Objects
############

******
Window
******

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
title                              A plaintext string | A               """Untitled           
                                   FormattedText object                 Window"""             
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
color                              A string description of the color    white                 
                                   (or keyword?); An rgb value          
                                   separated by spaces                  
action                             The name of a Python or Gooey        """"""                
                                   function to call when the object is  
                                   acted upon                           
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
font                               The string name of a font available  """Times New          
                                   in Gooey                             Roman"""              
fontSize                           A number indicating the font size    12                    
textColor                          A color (A string description or an  black                 
                                   rgb value)                           
===========  ====================  ===================================  ====================  

******
Button
******

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
title                              A plaintext string | A               """"""                
                                   FormattedText object                 
text                               A plaintext string | A               """Untitled           
                                   FormattedText object                 Button"""             
position                           A string description of the          center                
                                   position (or is this a keyword?);    
                                   An (x y) coordinate separated by a   
                                   space                                
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
action                             The name of a Python or Gooey        """"""                
                                   function to call when the object is  
                                   acted upon                           
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
===========  ====================  ===================================  ====================  

**********
Checkboxes
**********

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
title                              A plaintext string | A               """Untitled           
                                   FormattedText object                 Checkboxes"""         
options                            "A list separated by spaces          "*""Option 1""        
                                   containing (For Checkboxes etc) A    ""Option 2""          
                                   string preceded by a * if default    ""Option 3"""         
                                   selected; (For Menu) A menuItem      
                                   object; (For MenuItem) A menuItem    
                                   object | a terminal in the format    
                                   ""name"":action"                     
position                           A string description of the          center                
                                   position (or is this a keyword?);    
                                   An (x y) coordinate separated by a   
                                   space                                
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
===========  ====================  ===================================  ====================  

************
RadioButtons
************

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
title                              A plaintext string | A               """Untitled Radio     
                                   FormattedText object                 Buttons"""            
options                            "A list separated by spaces          "*""Option 1""        
                                   containing (For Checkboxes etc) A    ""Option 2""          
                                   string preceded by a * if default    ""Option 3"""         
                                   selected; (For Menu) A menuItem      
                                   object; (For MenuItem) A menuItem    
                                   object | a terminal in the format    
                                   ""name"":action"                     
position                           A string description of the          center                
                                   position (or is this a keyword?);    
                                   An (x y) coordinate separated by a   
                                   space                                
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
===========  ====================  ===================================  ====================  

********
DropDown
********

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
title                              A plaintext string | A               """Untitled Drop      
                                   FormattedText object                 Down"""               
options                            "A list separated by spaces          "*""Option 1""        
                                   containing (For Checkboxes etc) A    ""Option 2""          
                                   string preceded by a * if default    ""Option 3"""         
                                   selected; (For Menu) A menuItem      
                                   object; (For MenuItem) A menuItem    
                                   object | a terminal in the format    
                                   ""name"":action"                     
position                           A string description of the          center                
                                   position (or is this a keyword?);    
                                   An (x y) coordinate separated by a   
                                   space                                
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
===========  ====================  ===================================  ====================  

****
Text
****

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
text                               A plaintext string | A               """Text"""            
                                   FormattedText object                 
position                           A string description of the          center                
                                   position (or is this a keyword?);    
                                   An (x y) coordinate separated by a   
                                   space                                
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
color                              A string description of the color    white                 
                                   (or keyword?); An rgb value          
                                   separated by spaces                  
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
===========  ====================  ===================================  ====================  

*************
FormattedText
*************

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
text                               A plaintext string | A               """Formatted Text"""  
                                   FormattedText object                 
font                               The string name of a font available  """Times New          
                                   in Gooey                             Roman"""              
fontSize                           A number indicating the font size    12                    
textColor                          A color (A string description or an  black                 
                                   rgb value)                           
===========  ====================  ===================================  ====================  

*******
TextBox
*******

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
title                              A plaintext string | A               """Untitled Text      
                                   FormattedText object                 Box"""                
text                               A plaintext string | A               """Type here"""       
                                   FormattedText object                 
position                           A string description of the          center                
                                   position (or is this a keyword?);    
                                   An (x y) coordinate separated by a   
                                   space                                
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
===========  ====================  ===================================  ====================  

****
Menu
****

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
options                            "A list separated by spaces          menuItem1 menuItem2   
                                   containing (For Checkboxes etc) A    menuItem3             
                                   string preceded by a * if default    
                                   selected; (For Menu) A menuItem      
                                   object; (For MenuItem) A menuItem    
                                   object | a terminal in the format    
                                   ""name"":action"                     
position                           A string description of the          menuBar               
                                   position (or is this a keyword?);    
                                   An (x y) coordinate separated by a   
                                   space                                
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
===========  ====================  ===================================  ====================  

********
MenuItem
********

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
title                              A plaintext string | A               """Untitled Menu      
                                   FormattedText object                 Item"""               
options                            "A list separated by spaces          """Option 1""         
                                   containing (For Checkboxes etc) A    ""Option 2""          
                                   string preceded by a * if default    ""Option 3"""         
                                   selected; (For Menu) A menuItem      
                                   object; (For MenuItem) A menuItem    
                                   object | a terminal in the format    
                                   ""name"":action"                     
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
===========  ====================  ===================================  ====================  

******
Search
******

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
text                               A plaintext string | A               """Search"""          
                                   FormattedText object                 
position                           A string description of the          center                
                                   position (or is this a keyword?);    
                                   An (x y) coordinate separated by a   
                                   space                                
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
===========  ====================  ===================================  ====================  

*****
Image
*****

Attributes
==========

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
title                              A plaintext string | A               """"""                
                                   FormattedText object                 
text                               A plaintext string | A               """Image Caption"""   
                                   FormattedText object                 
position                           A string description of the          center                
                                   position (or is this a keyword?);    
                                   An (x y) coordinate separated by a   
                                   space                                
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
source                             A string containing a path/filename  defaultIcon           
===========  ====================  ===================================  ====================  

