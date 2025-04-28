def Trithemius_Decrypt(c):
    dec = ''
    for i in range(len(c)):
        char_cipher = c[i]
        if char_cipher.isalpha():
           dec += chr((((ord(char_cipher) - 0x41) - i) % 26) + 0x41)
        else : 
            dec += char_cipher
    return dec

flag = 'DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL'
print('HTB{'+ Trithemius_Decrypt(flag) + '}')
