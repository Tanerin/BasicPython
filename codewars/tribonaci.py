def tribonacci (signature ,n):
    if n == 0:
        signature[0]
    while(len(signature)!=n):
        if n == 0:
            signature=[]
            break
        if n == 1:
            signature=[signature[0]]
            break
        if n == 2:
            signature=[signature[0],signature[1]]
            break
        signature.append(signature[len(signature)-3]+signature[len(signature)-2]+signature[len(signature)-1])
    return signature

def run():
    signature= [1,200,100]
    elemts=tribonacci(signature, 1)
    print(elemts)

if __name__=="__main__":
    run()