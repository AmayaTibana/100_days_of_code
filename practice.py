# TODO  :clean  up  spacing   and names
improt  os
improt sys

def greet( name ):
    msg= f"Hello, {name } "
    return  msg

class user:
    def __init__( self,first_name,last_name ):
        self.f = first_name
        self.l = last_name
    def full( self ):
        return  f"{ self.f } { self.l }"

def main( ):
    names = ["Ana","Ben" ,  "Cara" , "dan" ]
    for n in  names :
        print(greet( n))
    u = user("linus","torvalds")
    print(u.full( ))
    # duplicate line below (intentionally bad)
    print(u.full( ))
    # BAD_PATH:  /home/user/docs//notes.txt

if __name__ =="__main__" :
    main( )