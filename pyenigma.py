rotors = []
reverseRotors = []

reflector = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
plugBoard = []
selectedRotor = ['', '', '']
selectedReverseRotor = ['', '', '']

def drawEnigma():
    print("■■■■■ ■   ■ ■■■■■ ■■■■■ ■   ■   ■  ")
    print("■     ■■  ■   ■   ■     ■■ ■■  ■ ■ ")
    print("■■■■■ ■ ■ ■   ■   ■  ■■ ■ ■ ■ ■■■■■")
    print("■     ■  ■■   ■   ■   ■ ■   ■ ■   ■")
    print("■■■■■ ■   ■ ■■■■■ ■■■■■ ■   ■ ■   ■")
    print("")
    print("")
    print("")

def initialize():
  # Rotor Initialize
  rotors.append(['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'])
  rotors.append(['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'])
  rotors.append(['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'])
  rotors.append(['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B'])
  rotors.append(['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K'])
  rotors.append(['J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N', 'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W'])
  rotors.append(['N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B', 'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T'])
  rotors.append(['F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P', 'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V'])
  reverseRotors.append(['U', 'W', 'Y', 'G', 'A', 'D', 'F', 'P', 'V', 'Z', 'B', 'E', 'C', 'K', 'M', 'T', 'H', 'X', 'S', 'L', 'R', 'I', 'N', 'Q', 'O', 'J'])
  reverseRotors.append(['A', 'J', 'P', 'C', 'Z', 'W', 'R', 'L', 'F', 'B', 'D', 'K', 'O', 'T', 'Y', 'U', 'Q', 'G', 'E', 'N', 'H', 'X', 'M', 'I', 'V', 'S'])
  reverseRotors.append(['T', 'A', 'G', 'B', 'P', 'C', 'S', 'D', 'R', 'E', 'U', 'F', 'V', 'N', 'Z', 'H', 'Y', 'I', 'X', 'J', 'W', 'L', 'R', 'K', 'O', 'M'])
  reverseRotors.append(['H', 'Z', 'W', 'V', 'A', 'R', 'T', 'N', 'L', 'G', 'U', 'P', 'X', 'Q', 'C', 'E', 'J', 'M', 'B', 'S', 'K', 'D', 'Y', 'O', 'I', 'F'])
  reverseRotors.append(['Q', 'C', 'Y', 'L', 'X', 'W', 'E', 'N', 'F', 'T', 'Z', 'O', 'S', 'M', 'V', 'J', 'U', 'D', 'K', 'G', 'I', 'A', 'R', 'P', 'H', 'B'])
  reverseRotors.append(['S', 'K', 'X', 'Q', 'L', 'H', 'C', 'N', 'W', 'A', 'R', 'V', 'G', 'M', 'E', 'B', 'J', 'P', 'T', 'Y', 'F', 'D', 'Z', 'U', 'I', 'O'])
  reverseRotors.append(['Q', 'M', 'G', 'Y', 'V', 'P', 'E', 'D', 'R', 'C', 'W', 'T', 'I', 'A', 'N', 'U', 'X', 'F', 'K', 'Z', 'O', 'S', 'L', 'H', 'J', 'B'])
  reverseRotors.append(['Q', 'J', 'I', 'N', 'S', 'A', 'Y', 'D', 'V', 'K', 'B', 'F', 'R', 'U', 'H', 'M', 'C', 'P', 'L', 'E', 'W', 'Z', 'T', 'G', 'X', 'O'])

def convert_plug_board(target):
  if target in plugBoard:
    idx = plugBoard.index(target)
    if idx % 2 == 0:
      return plugBoard[idx + 1]
    else:
      return plugBoard[idx - 1]
  else:
    return target

initialize()

# Start of Main
drawEnigma()
rotorChecks = list(map(int, input("로터 3개를 왼쪽부터 순서대로 선택하세요 (1 ~ 8) ex) 1 2 3 : ").split()))

for i, rotorCheck in enumerate(rotorChecks):
  idx = rotorCheck - 1
  selectedRotor[i] = rotors[idx]
  selectedReverseRotor[i] = reverseRotors[idx]
print('')

print("반사판을 세팅하세요 ex) A C")
for i in range(13):
  reflChange1, reflChange2 = list(map(lambda s: ord(s) - 65, input(f"{i+1} 번째 세팅 : ").split()))

  reflector[reflChange1], reflector[reflChange2] = reflector[reflChange2], reflector[reflChange1]

pairs = 0
print('플러그보드를 세팅하세요 (종료는 q 입력) ex) A C')
while True:
  if pairs >= 13:
    break

  inp = input(f'{pairs+1} 번째 세팅 : ')
  if inp == 'q':
    break

  plug1, plug2 = inp.split()
  if (plug1 in plugBoard) or (plug2 in plugBoard):
    continue

  plugBoard[pairs * 2 : pairs * 2 + 1] = plug1, plug2

  pairs = pairs + 1


print('\n')

print('모든 세팅을 끝냈습니다.')
print('--------------------------------')

print(f'로터 세팅 : {rotorChecks[0]} {rotorChecks[1]} {rotorChecks[2]}\n')

print('반사판 세팅 : ', end='')
for i in range(26):
  print(f'{reflector[i]} ', end='')
print('\n')

raw_message = input('암호화할 문장을 적으십시오. : ')
message = [char for char in raw_message]

code = []

for i in range(len(message)):
  a0 = convert_plug_board(message[i])
  a1 = ord(a0) - 65
  a2 = ord(selectedRotor[2][a1]) - 65
  a3 = ord(selectedRotor[1][a2]) - 65
  a4 = ord(selectedRotor[0][a3]) - 65
  a5 = ord(reflector[a4]) - 65
  a6 = ord(selectedReverseRotor[0][a5]) - 65
  a7 = ord(selectedReverseRotor[1][a6]) - 65
  a8 = selectedReverseRotor[2][a7]
  result = convert_plug_board(a8)
  code.append(result)

for i in range(len(message)):
  print(code[i], end='')
print('\n')
