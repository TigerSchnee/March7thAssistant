from managers.translate_manager import _
from tasks.power.power import Power
from tasks.activity.doubleactivity import DoubleActivity


class PlanarFissure(DoubleActivity):
    def _run_instances(self, reward_count):
        # 暂未支持自动刷取模拟宇宙领取奖励
        Power.merge("immersifier")
