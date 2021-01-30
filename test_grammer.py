import language_check
tool = language_check.LanguageTool('en-US')
text = u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
matches = tool.check(text)
print('# of suggestions found: ', len(matches))
#print(matches[1])
counter = 0
for x in matches:
    print('--------------------------------------------------------------------------------------------')
    print('Suggestion: ', counter)
    print('Original sentence: ', x.context)
    print( ' '*(x.contextoffset +19),'^^^^^^')
    print('Suggestion: ', x.msg)
    counter = counter+1


