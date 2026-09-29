import math
import random

def cal():
    # Initialize history list to fix the undefined 'self.history' error
    history = [] 

    while True:
        print("\n" + "="*50)
        print("       PYTHON SCIENTIFIC-CALCULATOR         ")
        print("=" *50)
        print(" Select an Option:")
        print("   [1] [+] ADDITION   ")
        print("   [2] [-] SUBTRACTION   ")
        print("   [3] [*] MULTIPLICATION   ")
        print("   [4] [/] DIVISION   ")
        print("   [5] [log] LOGARITHM   ")
        print("   [6] [sin, cos, tan] TRIGONOMETRY   ")
        print("   [7] [CI] COMPOUND INTEREST CALCULATOR    ")
        print("   [8] UNIT CONVERTER  (uniconv)   ")
        print("   [9] POWER AND SQUARE ROOT ")
        print("   [10] Numeric System Converter")
        print("   [11] Show History")
        print("   [0] back to main menu   ")
        print("="*50)
        print("\n")
 
        choice = input("ENTER THE CHOICE [0-11]-----").strip()

        # 0 return to main menu
        if choice == "0":
            print('\nReturning....')
            break
            
        # 1 addition
        elif choice == '1':
            a = float(input("enter first no. "))
            b = float(input("enter second no. "))
            c = (a+b)
            print("ANS IS ->>> " , c )
            history.append(f"{a} + {b} = {c}")

        # substraction
        elif choice == '2':
            a = float(input("enter first no. "))
            b = float(input("enter second no. "))
            c = (a-b)
            print("ANS IS ->>> " , c )
            history.append(f"{a} - {b} = {c}")

        # multiplication
        elif choice == '3':
            a = float(input("enter first no. "))
            b = float(input("enter second no. "))
            c = (a*b)
            print("ANS IS ->>> " , c )
            history.append(f"{a} * {b} = {c}")

        # division
        elif choice == '4':
            a = float(input("enter first no. "))
            b = float(input("enter second no. "))
            if b == 0:
                c = "INFINITY"
            else:
                c = (a/b)
            print("ANS IS ->>> " , c )
            history.append(f"{a} / {b} = {c}")

        # log
        elif choice == "5":
            x = float(input("enter the value of x (x>0)"))
            if x <= 0:
                print("MATHEMATICAL ERROR... {I thought u know that log(x) is defined only for x>0}")
            else:
                base_inp = input("enter the b [nothing means default 10 ] >>>").strip()
                if base_inp == "":
                    base = 10.0
                else:
                    base = float(base_inp)

                if base <= 0 or base == 1:
                    print("MATHEMATICAL ERROR... {base must be +ve and not equal to 1}")
                else:
                    c = math.log(x, base)
                    print("ANS IS ->>> ", c)
                    history.append(f"log base {base} of {x} = {c}")

        # 6 TRIGONOMETRY OPERATIONS
        elif choice == "6":
            print("choose: [s] sin , [c] cos , [t] tan >>> ")
            t_choice = input("select ->>> ").strip()
            deg = float(input("enter angles in degrees >>> "))
            rad = math.radians(deg)
            if t_choice == "s":
                c = math.sin(rad)
                print("ANS IS ->>> ", c)
                history.append(f"sin({deg}) = {c}")
            elif t_choice == "c":
                c = math.cos(rad)
                print("ANS IS ->>> ", c)
                history.append(f"cos({deg}) = {c}")
            elif t_choice == "t":
                if deg % 180 == 90:
                    print("ANS IS ->>> UNDEFINED")
                else:
                    c = math.tan(rad)
                    print("ANS IS ->>> ", c)
                    history.append(f"tan({deg}) = {c}")
            else:
                print("Invalid trigonometry choice")

        # compound interest calculator
        elif choice == "7":
            p = float(input("enter principal amount (p)>>> "))
            r = float(input("enter annual rate in % (R) >>>"))
            t = float(input("enter the time period in yrs (t)>>>"))
            n = float(input("enter the compounding frequency (n)>>>"))

            total_amount = p*((1+(r/(100*n)))**(n*t))
            c = total_amount - p 
            print("Total Accrued Is ->>>",total_amount)
            print("Compound Interest Is ->>> ", c)
            history.append(f"CI: Principal {p}, Accrued {total_amount}")

        # [8] unit converter
        elif choice == "8":
            print("[1] C to F  [2] F to C  [3] KM to Miles  [4] KG to LBS")
            u_choice = input("select ->>> ").strip()

            if u_choice == "1":
                val = float(input("enter temp in °C >>> "))
                c = (val * 9/5) + 32
                print("ANS IS ->>> ", c, "°F")
            elif u_choice == "2":
                val = float(input("enter temp in °F >>> "))
                c = (val - 32) * 5/9
                print("Answer IS >>> ", c, "°C")
            elif u_choice == "3":
                val = float(input("enter km >>> "))
                c = val * 0.621371
                print("Answer IS >>> ", c, "miles")
            elif u_choice == "4":
                val = float(input("enter kg >>> "))
                c = val * 2.20462
                print("Answer IS >>> ", c, "lbs")
            else:
                print("arre bhai option to thik se chua a kar 🙄 ")

        # [9] power and root
        elif choice == "9":
            print("[1] power and [2] square root ")
            p_choose = input("select >>>>").strip()
            if p_choose == "1":
                x = float(input("enter the base x >>>"))
                y = float(input("enter the exponent y >>>"))
                c = x**y
                print("Answer IS >>> ", c)
                history.append(f"{x}^{y} = {c}")
            elif p_choose == "2":
                x = float(input("enter number x >>> "))
                if x < 0:
                    print("Math Error: Cannot take square root of negative number")
                else:
                    c = math.sqrt(x)
                    print("Answer IS >>> ", c)
                    history.append(f"sqrt({x}) = {c}")
            else:
                print("Invalid option")

        # [10] Number System Converter
        elif choice == "10":
            print("\n" + "-" * 35)
            print("     NUMBER SYSTEM CONVERTER")
            print("-" * 35)
            print(" [1] BINARY TO DECIMAL")
            print(" [2] DECIMAL TO BINARY")
            print(" [3] DECIMAL TO OCTAL")
            print(" [4] DECIMAL TO HEXADECIMAL")
            print(" [5] BINARY TO OCTAL")
            print(" [6] BINARY TO HEXADECIMAL")
            print(" [7] Back ")
            print("-" * 35)

            sub_choice = input("Select conversion (1-6) >>> ").strip()

            # 1. Binary to Decimal
            if sub_choice == "1":
                b_str = input("Enter binary number >>> ").strip()
                if not all(ch in "01" for ch in b_str):
                    print("Error: Input must contain only 0s and 1s.")
                else:
                    b_num = int(b_str)
                    decimal = 0
                    power = 0
                    while b_num > 0:
                        digit = b_num % 10
                        decimal += digit * (2 ** power)
                        b_num = b_num // 10
                        power += 1
                    print("Answer IS >>>", decimal)

            # 2. Decimal to Binary
            elif sub_choice == "2":
                n = int(input("Enter decimal number >>> "))
                if n == 0:
                    print("Answer IS >>> 0")
                else:
                    binary_str = ""
                    temp = n
                    while temp > 0:
                        rem = temp % 2
                        binary_str = str(rem) + binary_str
                        temp = temp // 2
                    print("Answer IS >>>", binary_str)

            # 3. Decimal to Octal
            elif sub_choice == "3":
                n = int(input("Enter decimal number >>> "))
                if n == 0:
                    print("Answer IS >>> 0")
                else:
                    octal_str = ""
                    temp = n
                    while temp > 0:
                        rem = temp % 8
                        octal_str = str(rem) + octal_str
                        temp = temp // 8
                    print("Answer IS >>>", octal_str)

            # 4. Decimal to Hexadecimal
            elif sub_choice == "4":
                n = int(input("Enter decimal number >>> "))
                if n == 0:
                    print("Answer IS >>> 0")
                else:
                    hex_digits = "0123456789ABCDEF"
                    hex_str = ""
                    temp = n
                    while temp > 0:
                        rem = temp % 16
                        hex_str = hex_digits[rem] + hex_str
                        temp = temp // 16
                    print("Answer IS >>>", hex_str)

            # 5. Binary to Octal
            elif sub_choice == "5":
                b_str = input("Enter binary number >>> ").strip()
                if not all(ch in "01" for ch in b_str):
                    print("Error: Input must contain only 0s and 1s.")
                else:
                    b_num = int(b_str)
                    decimal = 0
                    power = 0
                    while b_num > 0:
                        digit = b_num % 10
                        decimal += digit * (2 ** power)
                        b_num = b_num // 10
                        power += 1

                    if decimal == 0:
                        print("Answer IS >>> 0")
                    else:
                        octal_str = ""
                        temp = decimal
                        while temp > 0:
                            rem = temp % 8
                            octal_str = str(rem) + octal_str
                            temp = temp // 8
                        print("Answer IS >>>", octal_str)

            # 6. Binary to Hexadecimal
            elif sub_choice == "6":
                b_str = input("Enter binary number >>> ").strip()
                if not all(ch in "01" for ch in b_str):
                    print("Error: Input must contain only 0s and 1s.")
                else:
                    b_num = int(b_str)
                    decimal = 0
                    power = 0
                    while b_num > 0:
                        digit = b_num % 10
                        decimal += digit * (2 ** power)
                        b_num = b_num // 10
                        power += 1

                    if decimal == 0:
                        print("Answer IS >>> 0")
                    else:
                        hex_digits = "0123456789ABCDEF"
                        hex_str = ""
                        temp = decimal
                        while temp > 0:
                            rem = temp % 16
                            hex_str = hex_digits[rem] + hex_str
                            temp = temp // 16
                        print("Answer IS >>>", hex_str)
            elif sub_choice == "7" or sub_choice == "0":
                pass
            else:
                print("Invalid selection! Please choose between 1 and 6.")

        # [11] History 
        elif choice == "11":
            print("\n--- History ---")
            if not history:
                print("No calculations yet.")
            else:
                for item in history:
                    print(item)
                    
        else:
            print("Invalid choice! Please select 0 to 11.")     

if __name__ == "__main__":
   cal()
