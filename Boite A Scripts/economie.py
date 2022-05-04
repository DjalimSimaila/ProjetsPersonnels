#!/bin/python3
import os


def p1():
    """
    """
    switch_that_cpu('off',6)
    switch_that_gpu("off")
    return

def switch_that_gpu(action):
    """
    docstring
    """
    if action == "on":
        os.system(f"""sudo bash -c "echo '\_SB_.PCI0.GPP0.VGA_._ON' > /proc/acpi/call""")
    else:
        os.system(f"""sudo bash -c "echo '\_SB_.PCI0.GPP0.VGA_._OFF' > /proc/acpi/call""")
    os.system("nvidia-smi")
    return

def switch_that_cpu(action, nombre=6):
    """
    Le nom est assez explicite, cette fonction met en offine des core du processeur
    ou bien la bonne grosse gtx pour economiser de la batterie
    """
    if action == "on":
        action = ('1', "allumé")
    else:
        action = ('0:', "eteint")
    for i in range(nombre):
        i = 7 - i
        code = os.system(
            "sudo bash -c 'echo "+action[0]+" > /sys/devices/system/cpu/cpu"+str(i)+"/online'")
        if code != 0:
            print("tas un pb bg")
        else:
            print("core numero "+str(i)+"- etat :"+action[1])
    os.system('grep "processor" /proc/cpuinfo')
    return


def manual():
    """
    """
    print("Allumer ou eteindre des cores?")
    action = input("[on][off]:")
    print("combien?")
    nb_de_core = int(input("[int] :"))
    print("eteindre le gpu?")
    actiongpu = input("[oui][non]:")
    switch_that_cpu(action,nb_de_core)
    switch_that_gpu(actiongpu)
    print("Voila")
    return



if __name__ == "__main__":
    dico_cmd = {
                'p1': p1,
                'p2': switch_that_cpu,
                'quit': exit,
                'manual' : manual,

                }
    print("""
    hello bg, suis le script qui est la pour preserver ta batterie .w.
    Que veux tu faire?
    p1 = 2 core + GPU off
    p2 = 4 core + GPU off
    manual = custom
    """)
    
    truc = input("[p1,p2,manual,quit]:")
    try:
        dico_cmd[truc]()
    except:
        pass