def Trithemius_Decrypt(c):
    dec = ''
    for i in range(len(c)):
        cipher = c[i]
        if cipher.isalpha():
           dec += chr((((ord(cipher) - 0x41) - i) % 26) + 0x41)
        else : 
            dec += cipher
    return dec

flag = 'DJF_CTA_ SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL'
print('HTB{'+ Trithemius_Decrypt(flag) + '}')
