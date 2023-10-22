import os
import time

os.system("java -jar 'hapsigntoolv2.jar' sign -mode localjks -privatekey harmonyos-demo "
          "-inputFile 'unsign-harmonyos-demo.hap' -outputFile "
          "'home/harmonyos/HarmonyOS/APP/sign-harmonyos-demo.hap' -signAlg SHA256withECDSA -keystore "
          "harmonyos-demo-debug.p12 -keystorepasswd ab123456 -keyaliaspasswd ab123456 -profile "
          "harmonyos-demo-debug.p7b -certpath harmonyos-demo-debug.cer -profileSigned 1")


def sign():
    os.system(f"java -jar 'home/harmonyos/HarmonyOS/APP/hapsigntoolv2.jar' sign -mode localjks -privatekey "
              "********* -inputFile '/' -outputFile "
              "'home/harmonyos/HarmonyOS/APP/sign-harmonyos-demo.hap' -signAlg SHA256withECDSA -keystore "
              "harmonyos-demo-debug.p12 -keystorepasswd ab123456 -keyaliaspasswd ab123456 -profile "
              "harmonyos-demo-debug.p7b -certpath harmonyos-demo-debug.cer -profileSigned 1")
