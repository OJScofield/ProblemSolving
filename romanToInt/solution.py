class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        skip = False
        for i in range(len(s)) :
            if skip == False :
                if s[i] == 'I' :
                    if i == len(s) - 1 :
                        number += 1
                        skip = False
                    else :
                        if s[i+1] == 'V' :
                            number += 4
                            skip = True
                        elif s[i+1] == 'X' :
                            number += 9
                            skip = True
                        else :
                            number += 1
                            skip = False

                elif s[i] == 'V' :
                    number += 5

                elif s[i] == 'X' :
                    if i == len(s) - 1 :
                        number += 10
                        skip = False
                    else :
                        if s[i+1] == 'L' :
                            number += 40
                            skip = True
                        elif s[i+1] == 'C':
                            number += 90
                            skip = True
                        else :
                            number += 10
                            skip = False

                elif s[i] == 'L' :
                    number += 50
                    skip = False


                elif s[i] == 'C' :
                    if i == len(s) - 1 :
                        number += 100
                        skip = False
                    else :
                        if s[i+1] == 'D' :
                            number += 400
                            skip = True
                        elif s[i+1] == 'M' :
                            number += 900
                            skip = True
                        else :
                            number += 100
                            skip = False

                elif s[i] == 'D' :
                    number += 500
                    skip = False
                else :
                    number += 1000
                    skip = False

            else :
                skip = False
        return number
