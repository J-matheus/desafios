user= "matheus"
key= 1234

login= str(input("Informe o login do usuario: "))
senha= int(input("Informe o senha do usuario: "))

if login ==user and senha ==key:
    print("Acesso permitido")
else:
    print("Acesso negado "
          "\nConfira se seu login e senha estão corretos.")