""""

We have to implement Data Encryption Standard Algorithm

Tasks to complete

1. Convert text into binary
2. Convert the binary into 64 bit blocks  -- append with 0's if not 64 bit
3. Compute initial Permutation
4. Compute Final Permutation

Return Result

"""

""""
  Converting Text into binart and then
  converting it into 8 bits and then
  converting it into 64 bits -- if not 64 pad with 0's
"""

def desPlainTextBlock(text):

  # convert to binary
  binary_text = ''.join(format(ord(word),'08b') for word in text)

  # pad with 0's if binary text is less than 64
  if(len(binary_text)<64):

    for i in range(len(binary_text),64):
      binary_text += '0'

  result_text = []
  if(len(binary_text) > 64):
    blocks = len(binary_text) // 64
    remainder = len(binary_text) % 64

    a = 0
    b= 64
    for i in range(blocks):
      result_text.append(binary_text[a:b])
      a+=64
      b+=64

    # if last chunk is smaller than 64 append with 0's
    if(remainder != 0):

      last = binary_text[a:]
      result_text .append(last.ljust(64,'0'))
    # join the arrays
    return result_text

  return binary_text



## Performing Initital permutation

def desInitialPermutation(binary):

  IP_table =[58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

  # defining the function which replaces each bit with the corrosponding bit in the table

  """
      Converting 64 bits into table
  """


  table = ['0' for i in range(len(binary))]

  """
      Re-Shuffling the values of IP table and binary_table
  """

  for i in range(64):
    table[i] = binary[IP_table[i] -1]


  return ''.join(table)




# Final Permutation

def desFinalPermutation(binary):
  ## Performing Initital permutation

  IP_TABLE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
  ]
  # defining the function which replaces each bit with the corrosponding bit in the table

  """
      Converting 64 bits into table
  """


  table = ['0' for i in range(len(binary))]


  """
      Re-Shuffling the values of IP table and binary_table
  """

  for i in range(64):
    table[i] = binary[IP_TABLE[i] -1]


  return ''.join(table)



def convert_to_text(binary):
  message = ""

  for block in binary:
    for  i in range(0,64,8):
      
      byte = block[i:i+8]
      message += chr(int(byte,2))

  return message





def main():
  
  message = input("Enter the message   :  ")
  binary_text  = desPlainTextBlock(message)
  initialPermutation = []
  finalPermutation = []

  for i in range(len(binary_text)):
    permuted_block = desInitialPermutation(binary_text[i])
    final_block  = desFinalPermutation(permuted_block)
    initialPermutation.append(permuted_block)
    finalPermutation.append(final_block)

  print("Original Text : ",message)
  print("64 Bit Binary Block  : \n" ,binary_text )
  print("After Initial Permutation : \n\n" ,initialPermutation )
  print("Initial Converted to Text  : ",convert_to_text(initialPermutation))
  print()

  print("After Final Permutation : \n\n" ,finalPermutation )
  print("Final Converted to Text  : ",convert_to_text(finalPermutation))

  


if __name__ == "__main__":
    main()

