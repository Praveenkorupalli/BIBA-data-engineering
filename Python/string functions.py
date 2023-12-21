#capitalize

sentence_1 = "mY name is YUVRAJ"
sentence_2 = "MY name is Ansul"
  
capitalized_string = sentence_1.capitalize() 
print("Sentence 1 output -> ", capitalized_string) 
capitalized_string = sentence_2.capitalize() 
print("Sentence 2 output -> ", capitalized_string) 

#count

message = 'GFG KARLO HO JAYEGA'
print('Number of occurrence of G:', message.count('G'))

#Find

message = 'Yuvraj is my name'
print(message.find('is'))

#lower
message = 'HEXAFORHEXA IS A COMPUTER SCIENCE PORTAL'
print(message.lower())

#upper

message = 'HexaforHexa is a computer science portal'
print(message.upper())

#Replace

text = 'subway surfer'
replaced_text = text.replace('s', 't') 
print(replaced_text)

#join

text = ['Anshul', 'is', 'my', 'only', 'friend'] 
print(' '.join(text))

