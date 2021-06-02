# flake8: noqa

from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

class CarControllerParams:

  ACCEL_HYST_GAP = 0.02  # don't change accel command for small oscilalitons within this value
  ACCEL_MAX = 1.5
  ACCEL_MIN = -4.7
  ACCEL_SCALE = 4.0  # max(ACCEL_MAX, -ACCEL_MIN)

  STEER_MAX = 384    # 409 is the max, 255 is stock
  STEER_DELTA_UP = 3
  STEER_DELTA_DOWN = 7
  STEER_DRIVER_ALLOWANCE = 50
  STEER_DRIVER_MULTIPLIER = 2
  STEER_DRIVER_FACTOR = 1

class CAR:
  # genesis
  GENESIS = "GENESIS 2015-2016"
  GENESIS_G70 = "GENESIS G70 2018"
  GENESIS_G80 = "GENESIS G80 2017"
  GENESIS_G90 = "GENESIS G90 2017"
  GENESIS_G90_L = "GENESIS G90 LIMOUSINE"
  # hyundai
  ELANTRA = "HYUNDAI ELANTRA LIMITED ULTIMATE 2017"
  ELANTRA_GT_I30 = "HYUNDAI I30 N LINE 2019 & GT 2018 DCT"
  SONATA = "HYUNDAI SONATA 2020"
  SONATA_HEV = "HYUNDAI SONATA HEV 2020"
  SONATA19 = "HYUNDAI SONATA 2019"
  SONATA19_HEV = "HYUNDAI SONATA 2019 HEV"
  SONATA_LF_TURBO = "HYUNDAI SONATA LF TURBO"
  KONA = "HYUNDAI KONA 2019"
  KONA_EV = "HYUNDAI KONA EV 2019"
  KONA_HEV = "HYUNDAI KONA HEV 2019"
  IONIQ = "HYUNDAI IONIQ HYBRID PREMIUM 2017"
  IONIQ_EV_LTD = "HYUNDAI IONIQ ELECTRIC LIMITED 2019"
  SANTA_FE = "HYUNDAI SANTA FE LIMITED 2019"
  PALISADE = "HYUNDAI PALISADE 2020"
  VELOSTER = "HYUNDAI VELOSTER 2019"
  GRANDEUR_IG = "HYUNDAI GRANDEUR IG 2017"
  GRANDEUR_IG_HEV = "HYUNDAI GRANDEUR IG HEV 2019"
  GRANDEUR_IG_FL = "HYUNDAI GRANDEUR IG FL 2020"
  GRANDEUR_IG_FL_HEV = "HYUNDAI GRANDEUR IG FL HEV 2020"
  TUCSON_TL_SCC  = "HYUNDAI TUCSON TL SCC 2017"
  # kia
  FORTE = "KIA FORTE E 2018"
  K5 = "KIA K5 2019 & 2016"
  K5_HEV = "KIA K5 HYBRID 2017 & SPORTS 2019"
  SPORTAGE = "KIA SPORTAGE S 2020"  
  SORENTO = "KIA SORENTO GT LINE 2018"
  STINGER = "KIA STINGER GT2 2018"
  NIRO_EV = "KIA NIRO EV 2020 PLATINUM"
  NIRO_HEV = "KIA NIRO HEV 2018"
  CEED = "KIA CEED 2019"
  K7 = "KIA K7 2016-2019"
  K7_HEV = "KIA K7 HEV 2016-2019"
  SELTOS = "KIA SELTOS 2021"


# ex) CAR_FORCE_RECOGNITION = CAR.GRANDEUR_IG
CAR_FORCE_RECOGNITION = None

class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  GAP_DIST = 3
  CANCEL = 4

FINGERPRINTS = {
  # genesis
  CAR.GENESIS: [{}],
  CAR.GENESIS_G70: [{}],
  CAR.GENESIS_G80: [{}],
  CAR.GENESIS_G90: [{}],
  CAR.GENESIS_G90_L: [{}],
  # hyundai
  CAR.ELANTRA: [{}],
  CAR.ELANTRA_GT_I30: [{}],
  CAR.SONATA: [{}],
  CAR.SONATA_HEV: [{}],
  CAR.SONATA19: [{}],
  CAR.SONATA19_HEV: [{}],
  CAR.SONATA_LF_TURBO: [{}],
  CAR.KONA: [{}],
  CAR.KONA_EV: [{}],
  CAR.KONA_HEV: [{}],
  CAR.IONIQ: [{}],
  CAR.IONIQ_EV_LTD: [{}],
  CAR.SANTA_FE: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 6, 764: 8, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1183: 8, 1186: 2, 1191: 2, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1479: 8, 1990: 8, 1998: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8, 2015: 8
  }],
  CAR.PALISADE: [{}],
  CAR.VELOSTER: [{}], 
  CAR.GRANDEUR_IG: [{}],
  CAR.GRANDEUR_IG_HEV: [{}],
  CAR.GRANDEUR_IG_FL: [{6}],
  CAR.GRANDEUR_IG_FL_HEV: [{}],
  CAR.TUCSON_TL_SCC: [{}],
  # kia
  CAR.FORTE: [{}],
  CAR.K5: [{}],
  CAR.K5_HEV: [{}],
  CAR.SPORTAGE: [{}],
  CAR.SORENTO: [{}],
  CAR.STINGER: [{}],
  CAR.NIRO_EV: [{}],
  CAR.NIRO_HEV: [{}], 
  CAR.CEED: [{}],
  CAR.K7: [{}],
  CAR.K7_HEV: [{}],
  CAR.SELTOS: [{}],
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [832, 1156, 1191, 1342]
}

# Don't use these fingerprints for fingerprinting, they are still used for ECU detection
IGNORED_FINGERPRINTS = [CAR.VELOSTER, CAR.GENESIS_G70, CAR.KONA, CAR.CEED, CAR.SELTOS]

FW_VERSIONS = {
  # genesis
  CAR.GENESIS_G70: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00IK__ SCC F-CUP      1.00 1.02 96400-G9100         \xf1\xa01.02', ],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00\x00\x00\x00\x00\x00\x00', ],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81640F0051\x00\x00\x00\x00\x00\x00\x00\x00', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00IK  MDPS R 1.00 1.06 57700-G9420 4I4VL106', ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00IK  MFC  AT USA LHD 1.00 1.01 95740-G9000 170920', ],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x87VDJLT17895112DN4\x88fVf\x99\x88\x88\x88\x87fVe\x88vhwwUFU\x97eFex\x99\xff\xb7\x82\xf1\x81E25\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E25\x00\x00\x00\x00\x00\x00\x00SIK0T33NB2\x11\x1am\xda', ],
  },    
  # hyundai
  CAR.SONATA: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00DN8_ SCC FHCUP      1.00 1.00 99110-L0000         ',
      b'\xf1\x00DN8_ SCC F-CU-      1.00 1.00 99110-L0000         ',
    ],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x8758910-L0100\xf1\x00DN ESC \x06 104\x19\x08\x01 58910-L0100\xf1\xa01.04',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x87391162M003\xf1\xa0000F',
      b'\xf1\x87391162M003\xf1\xa00240',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x8756310L0010\x00\xf1\x00DN8 MDPS C 1.00 1.01 56310L0010\x00 4DNAC101\xf1\xa01.01',
      b'\xf1\x8756310-L0010\xf1\x00DN8 MDPS C 1.00 1.01 56310-L0010 4DNAC101\xf1\xa01.01',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.00 99211-L0000 190716',
      b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.01 99211-L0000 191016',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x00bcsh8p54  U903\x00\x00\x00\x00\x00\x00SDN8T16NB0z{\xd4v',
    ],
  },
  CAR.SONATA_HEV: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00DNhe SCC FHCUP      1.00 1.02 99110-L5000         ',
    ],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x8758910-L0100\xf1\x00DN ESC \x06 104\x19\x08\x01 58910-L0100\xf1\xa01.04',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x87391062J002\xf1\xa0000P',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x8756310-L5500\xf1\x00DN8 MDPS C 1.00 1.02 56310-L5500 4DNHC102\xf1\xa01.02',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00DN8HMFC  AT USA LHD 1.00 1.04 99211-L1000 191016',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x00PSBG2323  E09\x00\x00\x00\x00\x00\x00\x00TDN2H20SA5\x97R\x88\x9e',
    ],
  },  
  CAR.KONA: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00OS__ SCC F-CUP      1.00 1.00 95655-J9200         \xf1\xa01.00', ],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x816V5RAK00018.ELF\xf1\x00\x00\x00\x00\x00\x00\x00\xf1\xa01.05', ],
    (Ecu.engine, 0x7e0, None): [b'"\x01TOS-0NU06F301J02', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00OS  MDPS C 1.00 1.05 56310J9030\x00 4OSDC105', ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00OS9 LKAS AT USA LHD 1.00 1.00 95740-J9300 g21', ],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2VE051\x00\x00\xf1\x006U2V0_C2\x00\x006U2VE051\x00\x00DOS4T16NS3\x00\x00\x00\x00', ],
  },
  CAR.KONA_EV: {
    (Ecu.fwdRadar, 0x7D0, None): [b'\xf1\x00OSev SCC FNCUP      1.00 1.01 99110-K4000        \xf1\xa01.01'],
    (Ecu.esp, 0x7D1, None): [b'\xf1\xa02.06'],
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4000\x00 4OEDC104',
      b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4050\x00 4OEDC104',
    ],
    (Ecu.fwdCamera, 0x7C4, None): [b'\xf1\x00OSE LKAS AT KOR LHD 1.00 1.00 95740-K4100 W40'],
  },
  CAR.SANTA_FE: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00TM__ SCC F-CUP      1.00 1.02 99110-S2000         \xf1\xa01.02'],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00TM ESC \x02 100\x18\x030 58910-S2600\xf1\xa01.00',],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81606EA051\x00\x00\x00\x00\x00\x00\x00\x00'],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00TM  MFC  AT USA LHD 1.00 1.00 99211-S2000 180409'],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x87SBJWAA6562474GG0ffvgeTeFx\x88\x97\x88ww\x87www\x87w\x84o\xfa\xff\x87fO\xff\xc2 \xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS1\x00\x00\x00\x00'],
  },
  CAR.PALISADE: {
    (Ecu.fwdRadar, 0x7d0, None): [
      b'\xf1\x00LX2_ SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',
      b'\xf1\000LX2_ SCC F-CUP      1.00 1.05 99110-S8100         \xf1\xa01.05',
      b'\xf1\x00LX2 SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',
    ],
    (Ecu.esp, 0x7d1, None): [
      b'\xf1\x00LX ESC \v 102\x19\x05\a 58910-S8330\xf1\xa01.02',
      b'\xf1\x00LX ESC \v 103\x19\t\x10 58910-S8360\xf1\xa01.03',
      b'\xf1\x00LX ESC \x01 103\x19\t\x10 58910-S8360\xf1\xa01.03',
      b'\xf1\x00LX ESC \x01 103\x31\t\020 58910-S8360\xf1\xa01.03',
      b'\xf1\x00LX ESC \x0b 102\x19\x05\x07 58910-S8330',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x81640J0051\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\xf1\x81640K0051\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7d4, None): [
      b'\xf1\x00LX2 MDPS C 1,00 1,03 56310-S8020 4LXDC103',  # modified firmware
      b'\xf1\x00LX2 MDPS C 1.00 1.03 56310-S8020 4LXDC103',
    ],
    (Ecu.fwdCamera, 0x7c4, None): [
      b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.03 99211-S8100 190125',
      b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.05 99211-S8100 190909',
      b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.08 99211-S8100 200903',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x87LBLUFN650868KF36\xa9\x98\x89\x88\xa8\x88\x88\x88h\x99\xa6\x89fw\x86gw\x88\x97x\xaa\x7f\xf6\xff\xbb\xbb\x8f\xff+\x82\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8',
      b'\xf1\x87LBLUFN655162KF36\x98\x88\x88\x88\x98\x88\x88\x88x\x99\xa7\x89x\x99\xa7\x89x\x99\x97\x89g\x7f\xf7\xffwU_\xff\xe9!\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8',
      b'\xf1\x87LBLUFN731381KF36\xb9\x99\x89\x98\x98\x88\x88\x88\x89\x99\xa8\x99\x88\x99\xa8\x89\x88\x88\x98\x88V\177\xf6\xff\x99w\x8f\xff\xad\xd8\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\000bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8',
      b'\xf1\x87LDKVBN424201KF26\xba\xaa\x9a\xa9\x99\x99\x89\x98\x89\x99\xa8\x99\x88\x99\x98\x89\x88\x99\xa8\x89v\x7f\xf7\xffwf_\xffq\xa6\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
      b'\xf1\x87LDLVBN560098KF26\x86fff\x87vgfg\x88\x96xfw\x86gfw\x86g\x95\xf6\xffeU_\xff\x92c\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
    ],
  },
  CAR.VELOSTER: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00JS__ SCC H-CUP      1.00 1.02 95650-J3200         ', ],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00\x00\x00\x00\x00\x00\x00', ],
    (Ecu.engine, 0x7e0, None): [b'\x01TJS-JNU06F200H0A', ],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00JSL MDPS C 1.00 1.03 56340-J3000 8308', ],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00JS  LKAS AT USA LHD 1.00 1.02 95740-J3000 K32', ],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJS0T16NS1\xba\x02\xb8\x80', ],
  },
  # kia
  CAR.K5: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00JF__ SCC F-CUP      1.00 1.00 96400-D4110         '],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x00JF ESC \v 11 \x18\x030 58920-D5180',],
    (Ecu.engine, 0x7e0, None): [b'\x01TJFAJNU06F201H03'],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409'],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00JFA LKAS AT USA LHD 1.00 1.02 95895-D5000 h31'],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJF0T16NL0\t\xd2GW'],
  },
  CAR.K5_HEV: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00DEhe SCC H-CUP      1.01 1.02 96400-G5100         ',],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x816H6F4051\x00\x00\x00\x00\x00\x00\x00\x00',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00DE  MDPS C 1.00 1.09 56310G5301\x00 4DEHC109',],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00DEP MFC  AT USA LHD 1.00 1.01 95740-G5010 170424',],
    (Ecu.transmission, 0x7e1, None): [b"\xf1\x816U3J2051\x00\x00\xf1\x006U3H0_C2\x00\x006U3J2051\x00\x00PDE0G16NS2\xf4'\\\x91",],
  },
  CAR.STINGER: {
    (Ecu.fwdRadar, 0x7d0, None): [ b'\xf1\x00CK__ SCC F_CUP      1.00 1.01 96400-J5100         \xf1\xa01.01'],
    (Ecu.engine, 0x7e0, None): [ b'\xf1\x81640E0051\x00\x00\x00\x00\x00\x00\x00\x00',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\x00CK  MDPS R 1.00 1.04 57700-J5420 4C4VL104'],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00CK  MFC  AT USA LHD 1.00 1.03 95740-J5000 170822'],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x87VDHLG17118862DK2\x8awWwgu\x96wVfUVwv\x97xWvfvUTGTx\x87o\xff\xc9\xed\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
      b'\xf1\x87VDHLG17000192DK2xdFffT\xa5VUD$DwT\x86wveVeeD&T\x99\xba\x8f\xff\xcc\x99\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
    ],
  },  
  CAR.NIRO_EV: {
    (Ecu.fwdRadar, 0x7D0, None): [
      b'\xf1\x00DEev SCC F-CUP      1.00 1.03 96400-Q4100         \xf1\xa01.03',
      b'\xf1\x00DEev SCC F-CUP      1.00 1.00 99110-Q4000         \xf1\xa01.00',      
    ],
    (Ecu.esp, 0x7D1, None): [
      b'\xf1\xa01.06',
      b'\xf1\xa01.07',      
    ],
    (Ecu.eps, 0x7D4, None): [
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4000\x00 4DEEC105',
      b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4100\x00 4DEEC105',
    ],
    (Ecu.fwdCamera, 0x7C4, None): [
      b'\xf1\x00DEE MFC  AT USA LHD 1.00 1.03 95740-Q4000 180821',
      b'\xf1\x00DEE MFC  AT EUR LHD 1.00 1.00 99211-Q4000 191211',
    ],
  },
  CAR.CEED:  {
    (Ecu.fwdRadar, 0x7D0, None): [b'\xf1\000CD__ SCC F-CUP      1.00 1.02 99110-J7000         ', ],
    (Ecu.esp, 0x7D4, None): [b'\xf1\000CD  MDPS C 1.00 1.06 56310-XX000 4CDEC106', ],
    (Ecu.fwdCamera, 0x7C4, None): [b'\xf1\000CD  LKAS AT EUR LHD 1.00 1.01 99211-J7000 B40', ],
    (Ecu.engine, 0x7E0, None): [b'\001TCD-JECU4F202H0K', ],
    (Ecu.transmission, 0x7E1, None): [b'\xf1\x816U2V7051\000\000\xf1\0006U2V0_C2\000\0006U2V7051\000\000DCD0T14US1\000\000\000\000', ],
    (Ecu.esp, 0x7D1, None): [b'\xf1\000CD ESC \003 102\030\b\005 58920-J7350', ],
  },
  CAR.SELTOS: {
    (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x8799110Q5100\xf1\000SP2_ SCC FHCUP      1.01 1.05 99110-Q5100         \xf1\xa01.05',],
    (Ecu.esp, 0x7d1, None): [b'\xf1\x8758910-Q5450\xf1\000SP ESC \t 101\031\t\005 58910-Q5450\xf1\xa01.01',],
    (Ecu.engine, 0x7e0, None): [b'\xf1\x81616D2051\000\000\000\000\000\000\000\000',],
    (Ecu.eps, 0x7d4, None): [b'\xf1\000SP2 MDPS C 1.00 1.04 56300Q5200          ',],
    (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\000SP2 MFC  AT USA LHD 1.00 1.04 99210-Q5000 191114',],
    (Ecu.transmission, 0x7e1, None): [b'\xf1\x87CZLUB49370612JF7h\xa8y\x87\x99\xa7hv\x99\x97fv\x88\x87x\x89x\x96O\xff\x88\xff\xff\xff.@\xf1\x816V2C2051\000\000\xf1\0006V2B0_C2\000\0006V2C2051\000\000CSP4N20NS3\000\000\000\000',],
  },
  CAR.K7: {
    (Ecu.eps, 0x7d4, None): [b'\xf1\000YG  MDPS C 1.00 1.01 56310F6350\000 4YG7C101',],
  },
}

CHECKSUM = {
  "crc8": [CAR.SANTA_FE, CAR.SONATA, CAR.PALISADE, CAR.SONATA_HEV, CAR.SELTOS],
  "6B": [CAR.SORENTO, CAR.GENESIS],
}

FEATURES = {
  # Use Cluster for Gear Selection, rather than Transmission
  "use_cluster_gears": {CAR.ELANTRA, CAR.KONA, CAR.ELANTRA_GT_I30, CAR.K7, CAR.NIRO_HEV, CAR.GRANDEUR_IG, CAR.GRANDEUR_IG_FL},

  # Use TCU Message for Gear Selection
  "use_tcu_gears": {CAR.K5, CAR.SONATA19, CAR.VELOSTER, CAR.SONATA_LF_TURBO, CAR.TUCSON_TL_SCC},

  # Use E_GEAR Message for Gear Selection
  "use_elect_gears": {CAR.K5_HEV, CAR.IONIQ_EV_LTD, CAR.KONA_EV, CAR.KONA_HEV, CAR.SONATA_HEV, CAR.NIRO_EV, CAR.K7_HEV,
                      CAR.GRANDEUR_IG_HEV, CAR.GRANDEUR_IG_FL_HEV},

  # Use E_EMS11 Message for Gas and Brake for Hybrid/ELectric
  "use_elect_ems": {CAR.K5_HEV, CAR.IONIQ_EV_LTD, CAR.KONA_EV, CAR.KONA_HEV, CAR.SONATA_HEV, CAR.NIRO_EV, CAR.K7_HEV,
                    CAR.GRANDEUR_IG_HEV, CAR.GRANDEUR_IG_FL_HEV},

  # send LFA MFA message for new HKG models
  "send_lfa_mfa": {CAR.SONATA, CAR.PALISADE, CAR.SONATA_HEV, CAR.SANTA_FE, CAR.NIRO_EV, CAR.GRANDEUR_IG_FL, CAR.GRANDEUR_IG_FL_HEV,
                   CAR.SELTOS, CAR.KONA_EV, CAR.KONA_HEV, CAR.TUCSON_TL_SCC},

  "has_scc13": {},
  "has_scc14": {},

  # these cars use the FCA11 message for the AEB and FCW signals, all others use SCC12
  "use_fca": {CAR.SONATA, CAR.ELANTRA, CAR.ELANTRA_GT_I30, CAR.STINGER, CAR.IONIQ, CAR.KONA, CAR.KONA_EV, CAR.FORTE,
              CAR.PALISADE, CAR.GENESIS_G70, CAR.SANTA_FE, CAR.SELTOS},

  "use_blinker_flash": {CAR.SONATA_LF_TURBO},

  "use_ldws": False,
}

DBC = {
  # genesis
  CAR.GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G70: dbc_dict('hyundai_kia_generic', None),  
  CAR.GENESIS_G80: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G90: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G90_L: dbc_dict('hyundai_kia_generic', None),
  # hyundai
  CAR.ELANTRA: dbc_dict('hyundai_kia_generic', None),
  CAR.ELANTRA_GT_I30: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA19: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA19_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_LF_TURBO: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV_LTD: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTA_FE: dbc_dict('hyundai_kia_generic', None),
  CAR.PALISADE: dbc_dict('hyundai_kia_generic', None),
  CAR.VELOSTER: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_IG: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_IG_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_IG_FL: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_IG_FL_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.TUCSON_TL_SCC: dbc_dict('hyundai_kia_generic', None),
  # kia
  CAR.FORTE: dbc_dict('hyundai_kia_generic', None),
  CAR.K5: dbc_dict('hyundai_kia_generic', None),
  CAR.K5_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SPORTAGE: dbc_dict('hyundai_kia_generic', None),  
  CAR.SORENTO: dbc_dict('hyundai_kia_generic', None),
  CAR.STINGER: dbc_dict('hyundai_kia_generic', None),  
  CAR.NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.CEED: dbc_dict('hyundai_kia_generic', None),
  CAR.K7: dbc_dict('hyundai_kia_generic', None),
  CAR.K7_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.SELTOS: dbc_dict('hyundai_kia_generic', None),
}

STEER_THRESHOLD = 150




def main():
  for member, value in vars(CAR).items():
    if not member.startswith("_"):
      print(value)


if __name__ == "__main__":
  main()
