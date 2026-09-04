# -*- coding: utf-8 -*-
from core.djm import Djm
# from core.gas import Gas
from core.gyro import MIru
from core.gyro import CeIru
from core.gps import Gps
from core.mission_controller import MissionController
# from core.mission_obc import MissionObc
from core.obc import Obc
# from core.pbi import Pbi
from core.pcu import Pcu
# from core.pdcu import Pdcu
# from core.power_shot import PowerShot
from core.rw import Rw
# from core.spaceware_micro import SpacewareMicro
from core.stt import Stt
from core.attitude_control import AttitudeControl


class MarviHkData(object):
    """衛星の全てのコンポーネントの情報(HKデータ)を保持するクラス。"""

    DJM_NUM = 5
    RW_NUM = 4
    STT_NUM = 4

    HK_SIZE = (
        Obc.HK_SIZE
        + AttitudeControl.HK_SIZE
        + Pcu.HK_SIZE
        # + Pdcu.HK_SIZE
        # + MissionObc.HK_SIZE
        + Djm.HK_SIZE * DJM_NUM
        + CeIru.HK_SIZE
        + MIru.HK_SIZE
        + Rw.HK_SIZE * RW_NUM
        + Stt.HK_SIZE * STT_NUM
        + Gps.HK_SIZE
        # + Gas.HK_SIZE
        # + Pbi.HK_SIZE
        # + SpacewareMicro.HK_SIZE
        # + PowerShot.HK_SIZE
        + MissionController.HK_SIZE
    )

    print("MARVI HK_SIZE: %d" % HK_SIZE)

    def __init__(self):
        super(MarviHkData, self).__init__()
        self.obc = Obc()
        self.djm = [Djm(djm_id) for djm_id in range(1, 1 + self.DJM_NUM)]
        self.pcu = Pcu()
        # self.pdcu = Pdcu()
        # self.mission_obc = MissionObc()
        self.rw = [Rw(rw_id) for rw_id in range(self.RW_NUM)]
        self.ce_iru = CeIru()
        self.m_iru = MIru()
        self.stt = [Stt(stt_id) for stt_id in range(self.STT_NUM)]
        self.gps = Gps()
        # self.gas = Gas()
        # self.pbi = Pbi()
        # self.spaceware_micro = SpacewareMicro()
        self.att = AttitudeControl()
        # self.ps = PowerShot()
        self.mission = MissionController()

