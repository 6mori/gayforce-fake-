from . import sword_guy
from .. import constants as c


class Guan_gong(sword_guy.SwordGuy):
    def __init__(self):
        super().__init__()

        self.name = c.GUAN_GONG
        self.sword_damage = 5
        self.HP = 500
        self.skill_damage = 50

    def skill(self, action_group):
        super().skill(c.GUAN_GONG, 10, 'gif')
        self.vincible=False
        # 冲刺
        if self.facing_right:
            self.rect.x += 6
        else:
            self.rect.x -= 6
            if self.skill_counter == 10 * c.SKILL_SPEED[c.GUAN_GONG] - 1:
                self.vincible=True


    def action(self, action_group):
        super().action(action_group, c.GUAN_GONG, 6, 'gif', (374 // 3, 157 // 2),c.CHARACTER_SIZE[c.GUAN_GONG])

    def setup_character_image_initial(self, character_name, postfix):
        super().setup_character_image_initial(c.GUAN_GONG, 'gif')

    def setup_character_image_stand(self, character_name, frame_number, postfix):
        super().setup_character_image_stand(c.GUAN_GONG, 7, 'gif')

    def setup_character_image_walk(self, character_name, frame_number, postfix):
        super().setup_character_image_walk(c.GUAN_GONG, 6, 'gif')
