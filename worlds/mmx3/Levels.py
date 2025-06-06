
from worlds.AutoWorld import World
from .Names import LocationName

location_id_to_level_id = {
    LocationName.intro_stage_boss:              [0x00, 0x200, 0x00],
    LocationName.intro_stage_mini_boss:         [0x00, 0x201, 0x00],
    LocationName.intro_stage_hp_1:              [0x00, 0x100, 0x00],
    LocationName.intro_stage_hp_2:              [0x00, 0x101, 0x00],
    LocationName.intro_stage_clear:             [0x01, 0x312, 0x1E],

    LocationName.blast_hornet_clear:            [0x01, 0x300, 0x02],
    LocationName.blast_hornet_boss:             [0x01, 0x202, 0x00],
    LocationName.blast_hornet_mini_boss:        [0x01, 0x203, 0x00],
    LocationName.blast_hornet_heart_tank:       [0x01, 0x002, 0x01],
    LocationName.blast_hornet_chimera_ride:     [0x01, 0x005, 0x01],
    LocationName.blast_hornet_helmet:           [0x01, 0x006, 0x10],
    LocationName.blast_hornet_hp_1:             [0x01, 0x102, 0x00],
    LocationName.blast_hornet_hp_2:             [0x01, 0x103, 0x00],

    LocationName.blizzard_buffalo_clear:        [0x02, 0x302, 0x0C],
    LocationName.blizzard_buffalo_boss:         [0x02, 0x204, 0x00],
    LocationName.blizzard_buffalo_heart_tank:   [0x02, 0x002, 0x02],
    LocationName.blizzard_buffalo_sub_tank:     [0x02, 0x003, 0x10],
    LocationName.blizzard_buffalo_legs:         [0x02, 0x004, 0x08],
    LocationName.blizzard_buffalo_hp_1:         [0x02, 0x104, 0x00],
    LocationName.blizzard_buffalo_hp_2:         [0x02, 0x105, 0x00],
    LocationName.blizzard_buffalo_hp_3:         [0x02, 0x106, 0x00],
    LocationName.blizzard_buffalo_hp_4:         [0x02, 0x107, 0x00],
    LocationName.blizzard_buffalo_hp_5:         [0x02, 0x108, 0x00],

    LocationName.gravity_beetle_clear:          [0x03, 0x304, 0x0A],
    LocationName.gravity_beetle_boss:           [0x03, 0x205, 0x00],
    LocationName.gravity_beetle_heart_tank:     [0x03, 0x002, 0x04],
    LocationName.gravity_beetle_frog_ride:      [0x03, 0x005, 0x08],
    LocationName.gravity_beetle_arms:           [0x03, 0x006, 0x20],
    LocationName.gravity_beetle_hp_1:           [0x03, 0x109, 0x00],
    LocationName.gravity_beetle_hp_2:           [0x03, 0x10A, 0x00],
    LocationName.gravity_beetle_energy_1:       [0x03, 0x10B, 0x00],
    LocationName.gravity_beetle_hp_3:           [0x03, 0x10C, 0x00],
    LocationName.gravity_beetle_hp_4:           [0x03, 0x10D, 0x00],
    LocationName.gravity_beetle_1up:            [0x03, 0x10E, 0x00],
    LocationName.gravity_beetle_hp_5:           [0x03, 0x10F, 0x00],
    LocationName.gravity_beetle_energy_2:       [0x03, 0x110, 0x00],
    LocationName.gravity_beetle_hp_6:           [0x03, 0x111, 0x00],

    LocationName.toxic_seahorse_clear:          [0x04, 0x306, 0x00],
    LocationName.toxic_seahorse_boss:           [0x04, 0x206, 0x00],
    LocationName.toxic_seahorse_mini_boss:      [0x04, 0x207, 0x00],
    LocationName.toxic_seahorse_heart_tank:     [0x04, 0x002, 0x08],
    LocationName.toxic_seahorse_kangaroo_ride:  [0x04, 0x005, 0x02],
    LocationName.toxic_seahorse_leg:            [0x04, 0x006, 0x80],
    LocationName.toxic_seahorse_hp_1:           [0x04, 0x112, 0x00],
    LocationName.toxic_seahorse_hp_2:           [0x04, 0x113, 0x00],
    LocationName.toxic_seahorse_hp_3:           [0x04, 0x114, 0x00],

    LocationName.volt_catfish_clear:            [0x05, 0x308, 0x04],
    LocationName.volt_catfish_boss:             [0x05, 0x208, 0x00],
    LocationName.volt_catfish_heart_tank:       [0x05, 0x002, 0x10],
    LocationName.volt_catfish_sub_tank:         [0x05, 0x003, 0x20],
    LocationName.volt_catfish_body:             [0x05, 0x004, 0x04],
    LocationName.volt_catfish_hp_1:             [0x05, 0x115, 0x00],
    LocationName.volt_catfish_hp_2:             [0x05, 0x116, 0x00],
    LocationName.volt_catfish_hp_3:             [0x05, 0x117, 0x00],
    LocationName.volt_catfish_energy_1:         [0x05, 0x118, 0x00],
    LocationName.volt_catfish_energy_2:         [0x05, 0x119, 0x00],
    LocationName.volt_catfish_hp_4:             [0x05, 0x11A, 0x00],
    LocationName.volt_catfish_energy_3:         [0x05, 0x11B, 0x00],
    LocationName.volt_catfish_hp_5:             [0x05, 0x11C, 0x00],

    LocationName.crush_crawfish_clear:          [0x06, 0x30A, 0x06],
    LocationName.crush_crawfish_boss:           [0x06, 0x209, 0x00],
    LocationName.crush_crawfish_heart_tank:     [0x06, 0x002, 0x20],
    LocationName.crush_crawfish_hawk_ride:      [0x06, 0x005, 0x04],
    LocationName.crush_crawfish_body:           [0x06, 0x006, 0x40],
    LocationName.crush_crawfish_hp_1:           [0x06, 0x11D, 0x00],
    LocationName.crush_crawfish_hp_2:           [0x06, 0x11E, 0x00],
    LocationName.crush_crawfish_hp_3:           [0x06, 0x11F, 0x00],
    LocationName.crush_crawfish_hp_4:           [0x06, 0x120, 0x00],
    LocationName.crush_crawfish_energy_1:       [0x06, 0x121, 0x00],
    LocationName.crush_crawfish_hp_5:           [0x06, 0x122, 0x00],
    LocationName.crush_crawfish_hp_6:           [0x06, 0x123, 0x00],
    LocationName.crush_crawfish_1up_1:          [0x06, 0x124, 0x00],
    LocationName.crush_crawfish_1up_2:          [0x06, 0x125, 0x00],

    LocationName.tunnel_rhino_clear:            [0x07, 0x30C, 0x0E],
    LocationName.tunnel_rhino_boss:             [0x07, 0x20A, 0x00],
    LocationName.tunnel_rhino_mini_boss:        [0x07, 0x20B, 0x00],
    LocationName.tunnel_rhino_heart_tank:       [0x07, 0x002, 0x40],
    LocationName.tunnel_rhino_sub_tank:         [0x07, 0x003, 0x40],
    LocationName.tunnel_rhino_helmet:           [0x07, 0x004, 0x01],
    LocationName.tunnel_rhino_energy_1:         [0x07, 0x126, 0x00],
    LocationName.tunnel_rhino_hp_1:             [0x07, 0x127, 0x00],

    LocationName.neon_tiger_clear:              [0x08, 0x30E, 0x08],
    LocationName.neon_tiger_boss:               [0x08, 0x20C, 0x00],
    LocationName.neon_tiger_mini_boss:          [0x08, 0x20D, 0x00],
    LocationName.neon_tiger_heart_tank:         [0x08, 0x002, 0x80],
    LocationName.neon_tiger_sub_tank:           [0x08, 0x003, 0x80],
    LocationName.neon_tiger_arms:               [0x08, 0x004, 0x02],
    LocationName.neon_tiger_hp_1:               [0x08, 0x128, 0x00],
    LocationName.neon_tiger_hp_2:               [0x08, 0x129, 0x00],
    LocationName.neon_tiger_hp_3:               [0x08, 0x12A, 0x00],

    LocationName.vile_stage_boss:               [0x09, 0x009, 0x00],
    LocationName.vile_stage_hp_1:               [0x09, 0x12B, 0x00],
    LocationName.vile_stage_hp_2:               [0x09, 0x12C, 0x00],
    LocationName.vile_stage_hp_3:               [0x09, 0x12D, 0x00],
    LocationName.vile_stage_hp_4:               [0x09, 0x12E, 0x00],
    LocationName.vile_stage_energy:             [0x09, 0x12F, 0x00],
    LocationName.vile_stage_hp_5:               [0x09, 0x130, 0x00],
    LocationName.vile_stage_hp_6:               [0x09, 0x131, 0x00],
    LocationName.vile_stage_hp_7:               [0x09, 0x132, 0x00],
    LocationName.vile_stage_1up:                [0x09, 0x133, 0x00],
    LocationName.vile_stage_hp_8:               [0x09, 0x134, 0x00],
    LocationName.vile_stage_hp_9:               [0x09, 0x135, 0x00],

    LocationName.doppler_lab_1_boss:            [0x0A, 0x20E, 0x00],
    LocationName.doppler_lab_1_mini_boss:       [0x0A, 0x20F, 0x00],
    LocationName.doppler_lab_1_hp_1:            [0x0A, 0x136, 0x00],
    LocationName.doppler_lab_1_energy:          [0x0A, 0x137, 0x00],
    LocationName.doppler_lab_1_hp_2:            [0x0A, 0x138, 0x00],

    LocationName.doppler_lab_2_boss:            [0x0B, 0x210, 0x00],
    #LocationName.doppler_lab_2_mini_boss:       [0x0B, 0x211, 0x00],

    LocationName.doppler_lab_3_boss:            [0x0C, 0x212, 0x00],
    LocationName.doppler_lab_3_blizzard_buffalo: [0x0C, 0x213, 0x00],
    LocationName.doppler_lab_3_toxic_seahorse:  [0x0C, 0x214, 0x00],
    LocationName.doppler_lab_3_tunnel_rhino:    [0x0C, 0x215, 0x00],
    LocationName.doppler_lab_3_volt_catfish:    [0x0C, 0x216, 0x00],
    LocationName.doppler_lab_3_crush_crawfish:  [0x0C, 0x217, 0x00],
    LocationName.doppler_lab_3_neon_tiger:      [0x0C, 0x218, 0x00],
    LocationName.doppler_lab_3_gravity_beetle:  [0x0C, 0x219, 0x00],
    LocationName.doppler_lab_3_blast_hornet:    [0x0C, 0x21A, 0x00],
    LocationName.doppler_lab_3_hp:              [0x0C, 0x139, 0x00],

    LocationName.bit_defeat:                    [0xFF, 0x00B, 0x00],
    LocationName.byte_defeat:                   [0xFF, 0x00A, 0x00],

    LocationName.victory:                       [0x0C, 0x00E, 0x00],
}
