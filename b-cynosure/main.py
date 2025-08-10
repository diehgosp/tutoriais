import subprocess

periodo = input("Digite um período: ").strip()

empresas = input("Digite o símbolo ou símbolos para várias empresa, ou deixe em branco para baixar os dados de todas as empresas: ").strip()

cmd = ["b-cynosure", periodo]
if empresas:
    cmd += ["-p"] + empresas.split()

subprocess.run(cmd)    

