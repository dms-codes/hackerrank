def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples_landing = [a+x for x in apples]
    count_apples, count_oranges = 0,0
    for apple_landing in apples_landing:
        if apple_landing in range(s,t+1):
            count_apples+=1
    oranges_landing = [b+x for x in oranges]
    for orange_landing in oranges_landing:
        if orange_landing in range(s,t+1):
            count_oranges+=1    
    print(count_apples)
    print(count_oranges)
