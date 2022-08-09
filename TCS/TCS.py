N= int(input("Enter an integer: "))

#Create a List of N element like 10,20,30,40...
Input= []
for i in range(1,N):
    Input.append(10*i)
print(Input)

K= int(input("Rotate up to: "))

def rightRotate(Input, K):
    #Create a list and enter first element
    Output = [Input[0]]
    # For Rotating the list by K, First append the last N-K element to the list.
    for k in range(len(Input) - K, len(Input)):
        Output.append(Input[k])
    #Append the remaining element to the list
    for item in range(1, len(Input) - K):
        Output.append(Input[item])
    return Output

print(rightRotate(Input, K))
