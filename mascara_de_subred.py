def bin_to_dec(binario):
    x, res = int((str(binario)).find("1")), []
    len_bin = len(str(binario)[x:])
    for i in range(len_bin, 0, -1):
        res.append((2**(i-1))*int(str(binario)[2*x - i]))
    return(sum(res))

try:
    while True:
        prefijo = int(input("Ingrese un prefijo de red: "))

        while prefijo < 0 or prefijo >32 or prefijo != int(prefijo):
            print("\033[31mingresa un valor entero dentro del rango\033[0m")
            prefijo = int(input("Ingrese un prefijo de entre 1 y 31: "))

        ip_binaria = "1" * prefijo + "0" * (32 - prefijo)
        res = []

        for i in range(0, 32, 8):
            x = ip_binaria[i: i + 8]
            res.append(str(bin_to_dec((x))))

        print(".".join(res))
except:
    print("\033[31mAlgo salió mal, intentalo de nuevo 🙌\033[0m")