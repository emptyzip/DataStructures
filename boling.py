i = total = strike_total = 0
frame =[]
score =[]
result=''

for i in range(10):
  while True :
    print("(입력)",i+1, end=" ")
    first, second = map(int, input( "프레임 : ").split())
    if first + second <= 10 and first > 0: #프레임 점수의 합이 10 이하이고 첫번째 핀이 0이 아닐때만
      score.append((first, second))

      f_total = first + second  #현재 프레임의 점수 계산
      if first == 10:
        result = '~'
      elif f_total == 10:
        result = '/'
      else:
        result = '-'
      frame.append((first, second, result, f_total)) #프레임에 결과 값 출력

      if i>0: #전값을 가져와야 하니까 i>0일 때
        prev_first, prev_second = score[i-1]
        if (prev_first+prev_second) == 10: #전 프레임이 스페어거나 스트라이크
          if prev_first < 10: #스페어
            f_total += first #현재 점수 + 첫번째 핀 수
            frame[i-1] = [prev_first, prev_second, '/', (prev_first+prev_second+first)] 
          if prev_first==10: #스트라이크
              if first < 10: #스트라이크가 아닌 경우 현재 프레임 점수 계산
                f_total += first+second
                frame[i-1] = [prev_first, prev_second, '~', (prev_first+first+second)]
              if i>1: # 전전 프레임 값을 가져올 수 있는 최소는 i > 1일 때
                prev_prev_first, prev_prev_second = score[i-2] ##전전 값
                if prev_prev_first==10: #전전 프레임도 스트라이크인지 체크
                  strike_total = 0 #스트라이크 점수 갱신을 위한 변수
                  strike_total += (prev_prev_first + (prev_first+prev_second) + (first)) 
                  f_total += (strike_total - prev_prev_first)
                  frame[i-2] = [prev_prev_first, prev_prev_second, '~', strike_total]

      total += f_total
      break
    else:
      print("잘못 입력하셨습니다. 다시 입력해주십시오. 각 프레임 점수의 합계는 10 이하여야 합니다.")

  print(frame)
  print("Total = ", total)
  if(i==9):
    #마지막 프레임의 값을 따로 변수에 저장
    lastFirst = first
    lastSecond = second

    if prev_first == 10: # 10프레임에서 for문이 끝나기 때문에 전전 점수 업데이트
      prev_total = prev_first+(first+second) #prev_total을 만들어서 아래에서도 사용
      frame[i-1] = [prev_first, prev_second, '~', prev_total] #프레임 업데이트

    if lastFirst == 10: #스트라이크
      print("Bonus 점수 2회 입력:", end=' ')
      first, second = map(int, input().split())
      f_total = lastFirst

      if first+second == 20: #10프레임과 보너스 두 번, 총 3번의 스트라이크인 경우
        f_total += lastFirst+first+second 
        if prev_first == 10: #전전이 스트라이크인 경우 보너스의 first값 더해주기 위해 체크
          prev_total += first
          frame[i-1] = [prev_first, prev_second, '~', prev_total]
      else:
        f_total += first+second #아닌 경우 보너스 점수 더해주기
      frame[i] = [lastFirst, lastSecond, '~', lastFirst+first+second]

    elif (lastFirst < 10) and (lastFirst+lastSecond == 10): # 마지막 프레임이 스페어인 경우
      print("Bonus 점수 1회 입력:", end=' ')
      first = int(input())
      f_total = first
      frame[i] = [lastFirst, lastSecond, '/', (lastFirst+lastSecond+first)]
    else: #스페어도 스트라이크도 아닌 경우
      break
    print(frame)
    total +=f_total
    print("Total = ", total)

  