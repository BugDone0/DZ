def sum_distance(from_n, to_n):
    return((from_n+to_n)*(to_n-from_n+1)/2 if from_n<to_n else (from_n+to_n)*(from_n-to_n+1)/2 )
def trim_and_repeat(str_input :str, offset :int,repetitions :int):
    return(str_input[offset*repetitions:])
sum_distance(int(input()),int(input()))
trim_and_repeat(input(),0,1)
