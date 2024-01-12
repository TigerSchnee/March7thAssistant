from managers.automation_manager import auto
from managers.translate_manager import _
from tasks.reward.rewardtemplate import RewardTemplate


class Assist(RewardTemplate):
    def run(self):
        if auto.click_element("./assets/images/assist/gift.png", "image", 0.9):
            auto.click_element("./assets/images/base/click_close.png", "image", 0.9, max_retries=10)
