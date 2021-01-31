import language_check
from google.cloud import vision
from pdfminer import input_for_text
from cloud_vision import input_for_text_vis
tool = language_check.LanguageTool('en-US')
text = input_for_text_vis
matches = tool.check(text)
print('Total # of suggestions found: ', len(matches))
print("\n \n")
#print(matches[1])
counter = 0
TGREEN =  '\033[32m' # Green Text
TRED =  '\033[31m' # Red Text

ENDC = '\033[m'
for x in matches:
    print('--------------------------------------------------------------------------------------------')
    # print("\033[0;37;40m Normal text\n")
    print(TGREEN +'Suggestion: ', ENDC, counter)
    print(TGREEN + 'Original sentence: ', ENDC, x.context)
    print( TRED, ' '*(x.contextoffset +19),'^^^^^^', ENDC)
    print(TGREEN,'Suggestion category: ', ENDC, x.category)
    print(TGREEN,'Suggestion: ', ENDC, x.msg)
    counter = counter+1


